import streamlit as st
import time, tempfile, os, pathlib
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from google import genai                             
from google.genai import types                       

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

# Streamlit UI
st.set_page_config(page_title="Multimodal Video Summarizer", page_icon="🎥")
st.title("Phidata Video‑Summarizer 🤖")

@st.cache_resource
def initialize_agent():
    return Agent(
        name="AI Video Summarizer",
        model=Gemini(id="gemini-2.5-flash"),
        tools=[],
        markdown=True,
    )

agent = initialize_agent()

video = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])

if video:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(video.read())
        video_path = tmp.name

    st.video(video_path)

    query = st.text_area(
        "What do you want to know about this video?",
        placeholder="Key moments, summary, …",
    )

    if st.button("🔍 Analyze"):
        if not query:
            st.warning("Enter a question first!")
        else:
            try:
                with st.spinner("Uploading to Gemini…"):
                    gfile = client.files.upload(file=video_path)
                    while gfile.state != "ACTIVE":
                        time.sleep(1)
                        gfile = client.files.get(name=gfile.name)

                analysis_prompt = (
                    f"Analyze the uploaded video and answer:\n{query}\n"
                    "Respond clearly and engagingly."
                )

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[analysis_prompt, gfile],
                )

                st.subheader("Answer")
                st.markdown(response.text)

            finally:
                pathlib.Path(video_path).unlink(missing_ok=True)
else:
    st.info("Upload a video to begin.")

st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)