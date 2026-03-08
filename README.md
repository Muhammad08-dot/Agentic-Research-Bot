# 🤖 Agentic Research Bot (CrewAI + Gemini)

An advanced AI-driven research assistant developed using **CrewAI** and **Google Gemini**. This bot coordinates a specialized team of AI agents to research, write, and review high-quality academic papers autonomously, specifically targeting a 20-30 page scope.

---

## 🚀 Features
* **Multi-Agent Orchestration:** Uses a Researcher, Writer, and Reviewer to ensure depth and academic quality.
* **20-Page Target:** Engineered to expand technical topics into comprehensive, detailed research papers.
* **Real-time Web Search:** Integrated with DuckDuckGo to fetch the latest 2026 industry trends and statistics.
* **Professional PDF Export:** Automatically generates structured PDFs including Abstract, Introduction, and References.

---

## 🛠️ Tech Stack
* **LLM:** Google Gemini 1.5/2.0 Flash.
* **Orchestration Framework:** CrewAI & LangChain.
* **Frontend:** Streamlit.
* **Search API:** DuckDuckGo Search.
* **PDF Generation:** FPDF2.

---

## 📖 How to Use (Step-by-Step Guide)

```text
1️⃣ Clone the Repository:
   git clone [https://github.com/Muhammad08-dot/Agentic-Research-Bot.git](https://github.com/Muhammad08-dot/Agentic-Research-Bot.git)
   cd Agentic-Research-Bot

2️⃣ Create a Virtual Environment:
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate

3️⃣ Install Dependencies:
   pip install -r requirements.txt

4️⃣ Setup API Key:
   - Get your Gemini API Key from Google AI Studio.
   - Enter it in the sidebar of the Streamlit app.

5️⃣ Run the Application:
   streamlit run app.py

6️⃣ Generate Your Paper:
   - Enter Topic: Input your Research Topic (e.g., "The Impact of AI on Finance").
   - Start Process: Click "Start Multi-Agent Process".
   - Monitor: Watch the VS Code Terminal to see the Agents collaborating.
   - Download: Get your final PDF once the process completes.
