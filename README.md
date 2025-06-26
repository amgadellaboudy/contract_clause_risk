# 📜 Clause-Risk GPT

**A GPT-powered contract assistant that identifies risky clauses in uploaded PDFs.**

This lightweight agent uses GPT-4o and LangChain to extract and score clauses from contracts, giving you a fast plain-English breakdown of legal and commercial risk.

---

## ✨ What It Does

- 🧾 Reads any contract PDF
- 🚨 Flags up to 8 risky clauses
- 🔢 Scores risk severity from 1 to 10
- 💬 Explains “why risky” in plain English
- 📤 Outputs a downloadable CSV report

---

## 🔧 Use Cases

- ✅ Founders reviewing partnership or vendor contracts  
- ✅ Legal teams automating first-pass risk triage  
- ✅ Procurement departments evaluating third-party terms  
- ✅ Anyone working with NDAs, MSAs, or SOWs

---

## 🚀 Demo (WIP)

> *“Upload a contract. In 30 seconds, get back a table of red flags, scores, and plain-English explanations.”*

![Demo](demo/demo.gif)

---

## 📦 Quickstart

You will need to source an OpenAI Api key to get started, you can source one from https://openai.com/api/
Once you have that key, create a .env file, in the same format as the .env.example file in the repo.
The rest is below:

```bash
# Clone the repo
git clone https://github.com/amgadellaboudy/ai-act-ready.git
cd ai-act-ready

# Set up a virtual environment (optional)
python -m venv venv

MacOS:
source venv/bin/activate

Windows:
.\venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 👋 Work With Me

I'm an AI engineer who specializes in building real-world, production-grade GPT agents and compliance copilots like this one. If you're:

- A company looking to integrate GPT into your product or internal workflows  
- A founder who needs a personalized AI assistant for your team or users  
- A legal, recruiting, or real estate firm exploring AI automation  

📩 I offer:
- Custom GPT builds trained on your data  
- Compliance-focused RAG agents  
- Lightweight AI audits to help you identify where LLMs can save time or money  

If you're interested in adapting this project—or building something custom from scratch—feel free to reach out.

📧 Email: [amgad.ellaboudy@gmail.com](mailto:amgad.ellaboudy@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/amgadellaboudy](https://www.linkedin.com/in/amgad-ellaboudy-aa596726/)
