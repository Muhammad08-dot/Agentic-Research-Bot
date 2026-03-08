# 🤖 Agentic Research Bot (CrewAI + Gemini)

An advanced AI-driven research assistant developed using **CrewAI** and **Google Gemini 2.0 Flash**. This bot coordinates a team of AI agents to research, write, and review high-quality academic papers (targeting 20+ pages) autonomously.

## 🚀 Features
- **Multi-Agent Orchestration:** Uses a Researcher, Writer, and Reviewer to ensure depth and quality.
- **20-Page Target:** Specifically designed to expand technical topics into comprehensive papers.
- **Real-time Web Search:** Integrated with DuckDuckGo for 2026 industry trends and statistics.
- **Professional PDF Export:** Automatically generates formatted PDFs with academic structures.
- **Frameworks:** Built with Streamlit, CrewAI, and LangChain.

## 🛠️ Tech Stack
- **LLM:** Google Gemini 1.5/2.0 Flash
- **Orchestration:** CrewAI & LangChain
- **Frontend:** Streamlit
- **Search:** DuckDuckGo Search API
- **PDF Generation:** FPDF2

## 📂 Project Structure
- `app.py`: Streamlit interface.
- `generator.py`: Core logic for Agent team and Tasks.

## 👤 Developer
**Muhammad Abdullah** *BS-AI (4th Semester)* *National University of Modern Languages (NUML)* *Roll No: 9249401*

## 🛠️ How to Use

Follow these steps to get the Agentic Research Bot running on your local machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/Muhammad08-dot/Agentic-Research-Bot.git](https://github.com/Muhammad08-dot/Agentic-Research-Bot.git)
cd Agentic-Research-Bot
2. Create a Virtual Environment
Bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Setup API Key
Get your Gemini API Key from Google AI Studio.

Enter it in the sidebar of the Streamlit app or set it in your environment variables.

5. Run the Application
Bash
streamlit run app.py
6. Generate Your Paper
Enter your Research Topic (e.g., "The Impact of AI on Finance").

Click "Start Multi-Agent Process".

Monitor the VS Code Terminal to see the Agents (Researcher, Writer, Reviewer) collaborating in real-time.

Download your final PDF once the process completes.

📂 Project Structure
app.py: Streamlit web interface.

generator.py: Core logic for Agent team coordination and task definitions.

searcher.py: Custom tool for real-time web searching.

pdf_exporter.py: Converts markdown agent output into a professional PDF.

requirements.txt: List of necessary Python packages.
