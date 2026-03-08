import streamlit as st
from generator import ResearchPaperGenerator
from pdf_exporter import PDFExporter
import sys

# Page Config
st.set_page_config(page_title="Agentic Research Bot", page_icon="🤖", layout="wide")

st.markdown("""
    <style>
    .agent-status { 
        background-color: #f0f2f6; 
        padding: 15px; 
        border-radius: 10px; 
        border-left: 5px solid #ff4b4b;
        font-family: monospace;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 CrewAI Research Agent")
st.info("Muhammad, ye naya system Agents (Researcher & Writer) use kar raha hai. Ye thora waqt lega lekin quality behtar hogi.")

# Sidebar
with st.sidebar:
    st.header("🔑 Authentication")
    api_key = st.text_input("Gemini API Key", type="password")
    st.markdown("---")
    st.write("Current Framework: **CrewAI**")
    st.write("Model: **Gemini 2.0 Flash**")

# Input
topic = st.text_input("📌 Research Topic", placeholder="Enter your topic here...")

if st.button("🚀 Start Multi-Agent Process", type="primary", use_container_width=True):
    if not api_key or not topic:
        st.error("❌ Please provide API Key and Topic!")
    else:
        # Placeholder for logs
        status_container = st.empty()
        status_container.markdown('<div class="agent-status">⏳ Initializing Agents...</div>', unsafe_allow_html=True)
        
        try:
            generator = ResearchPaperGenerator(api_key=api_key)
            
            # CrewAI execution
            with st.spinner("🕵️ Agents are working... (Researching & Writing)"):
                paper_data = generator.generate_full_paper(topic)
            
            # Export to PDF
            exporter = PDFExporter()
            pdf_file = exporter.export(topic, paper_data, "agent_research.pdf")
            
            st.success("✅ Paper Finished by Agents!")
            
            # Download
            with open(pdf_file, "rb") as f:
                st.download_button("📥 Download Agentic Research Paper", f.read(), f"{topic}_Agentic.pdf", "application/pdf")
            
            # Preview
            st.markdown("### 📄 Final Output Preview")
            st.markdown(paper_data["Full Research Paper"])

        except Exception as e:
            st.error(f"❌ Agent Error: {str(e)}")