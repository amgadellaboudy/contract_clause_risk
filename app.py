"""
Streamlit UI for Clause-Risk GPT
--------------------------------
Upload any contract PDF ➜ GPT highlights risky clauses,
scores them 1-10, and suggests improvements.
"""
import os
import csv
import streamlit as st
from dotenv import load_dotenv
from tools.risk_analyzer import analyze_contract_pdf

load_dotenv()
st.set_page_config(page_title="Clause-Risk GPT", layout="centered")
st.title("📜 Clause-Risk GPT")

uploaded_file = st.file_uploader("Upload contract (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Analyzing…"):
        results = analyze_contract_pdf(uploaded_file)

    # === Display results ===
    st.subheader("🔎 Risky Clauses")
    df = results.to_pandas()
    st.dataframe(df, use_container_width=True)

    # === Download CSV ===
    csv_path = "risk_analysis.csv"
    df.to_csv(csv_path, index=False, quoting=csv.QUOTE_ALL)
    st.download_button(
        label="Download CSV",
        data=open(csv_path, "rb").read(),
        file_name="clause_risk_report.csv",
        mime="text/csv",
    )

    # === Clean up temp files ===
    try:
        os.remove(csv_path)
    except OSError:
        pass
