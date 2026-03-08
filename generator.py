import os
import google.generativeai as genai
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from searcher import WebSearcher

class ResearchPaperGenerator:
    def __init__(self, api_key: str = None):
        # ✅ API Key Setup
        self.api_key = api_key or "ur api "
        os.environ["GOOGLE_API_KEY"] = self.api_key
        
        # CrewAI ko OpenAI key se rokne ke liye
        os.environ["OPENAI_API_KEY"] = "NA" 

        # ✅ 1. Pehle Models Check Karte Hain
        self.working_model = self._find_working_model()
        
        # ✅ 2. Phir LLM Initialize Karte Hain
        self.llm = ChatGoogleGenerativeAI(
            model=self.working_model, 
            google_api_key=self.api_key,
            temperature=0.7
        )
        self.searcher = WebSearcher()

    def _find_working_model(self):
        """Available models ki list check karke pehla working model nikalta hai"""
        genai.configure(api_key=self.api_key)
        print("🔍 Checking available models for your API Key...")
        
        try:
            available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            
            # Hum flash models ko priority dete hain
            for target in ["models/gemini-1.5-flash", "models/gemini-pro", "models/gemini-1.0-pro"]:
                if target in available_models:
                    print(f"✅ Found and using: {target}")
                    # LangChain ko sirf naam chahiye hota hai, 'models/' prefix ke baghair bhi chal jata hai
                    return target.replace("models/", "")
            
            # Agar kuch na mile to pehla wala pick kar lo
            return available_models[0].replace("models/", "")
        except Exception as e:
            print(f"⚠️ Could not list models: {e}. Falling back to default.")
            return "gemini-1.5-flash"

    def generate_full_paper(self, topic: str) -> dict:
        print(f"\n🚀 Starting CrewAI with model: {self.working_model}\n")

        # Agents
        researcher = Agent(
            role='Senior Research Analyst',
            goal=f'Find data for {topic}',
            backstory="Expert researcher.",
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

        writer = Agent(
            role='Academic Professor',
            goal=f'Write 20 pages on {topic}',
            backstory="Professional writer.",
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

        # Tasks
        search_task = Task(description=f"Research {topic}", expected_output="Facts.", agent=researcher)
        write_task = Task(description=f"Write paper on {topic}", expected_output="Markdown paper.", agent=writer, context=[search_task])

        # Crew
        crew = Crew(agents=[researcher, writer], tasks=[search_task, write_task], verbose=True)
        raw_result = crew.kickoff()
        
        return {"Full Research Paper": str(raw_result)}