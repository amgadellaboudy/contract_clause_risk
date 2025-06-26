"""
Core logic: extract text ➜ GPT risk assessment ➜ return Pydantic list
"""
import io
from typing import List
from pypdf import PdfReader
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from tools.schemas import ClauseRiskList

load_dotenv()
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# --- prompt ---
parser = PydanticOutputParser(pydantic_object=ClauseRiskList)
prompt = ChatPromptTemplate.from_template(
    """
    You are a senior contract lawyer. From the contract text below,
    identify up to 8 clauses that pose legal or commercial risk.
    For each risky clause, output:
      • clause_excerpt  (<=50 words)
      • risk_score      (1 = low, 10 = severe)
      • why_risky       (plain English, <=30 words)
      • suggested_change (<=20 words or empty string)

    Respond {format_instructions}
    Contract:
    =========
    {contract_text}
    =========
    """
)


# --- public API ---
def analyze_contract_pdf(file_obj) -> ClauseRiskList:
    """Accepts a Streamlit UploadedFile (BytesIO) -> returns ClauseRiskList"""
    text = _pdf_to_text(file_obj)
    formatted = prompt.format_prompt(
        contract_text=text[:12000],  # truncate to stay under token limits
        format_instructions=parser.get_format_instructions(),
    )
    resp = llm.invoke(formatted.to_messages())
    return parser.parse(resp.content)


# --- util ---
def _pdf_to_text(file_obj) -> str:
    if isinstance(file_obj, io.BytesIO):
        pdf = PdfReader(file_obj)
    else:  # assume Path-like
        pdf = PdfReader(open(file_obj, "rb"))
    pages = [p.extract_text() for p in pdf.pages]
    return "\n".join(pages)
