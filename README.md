# 🎥 Multimodal Video Chatbot using Google Gemini

An AI-powered web application that allows users to upload a video and interact with it using natural language queries. Powered by Google's Gemini 2.5 Flash multimodal model, the chatbot intelligently analyzes both the video and user input to generate context-aware responses.

---

## 🚀 Features

- 📁 Upload video files (`.mp4`, `.mov`, `.avi`)
- 💬 Ask conversational questions related to the video
- 🧠 Gemini 2.5 Flash processes both video + query context
- ⚡️ Real-time analysis and response
- 🔐 Secure API key handling via `.env`
- 🧹 Temporary file management with automatic cleanup
- 🖥️ User-friendly interface built with Streamlit

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit
- **AI Model:** Google Gemini 2.5 Flash via [Google GenAI SDK](https://pypi.org/project/google-genai/)
- **Agent Framework:** [Agno](https://pypi.org/project/agno/)
- **Others:** Python, dotenv, tempfile, pathlib

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/yourusername/multimodal-video-chatbot.git
cd multimodal-video-chatbot
```

### 2. Install Dependencies

Use a virtual environment (recommended):
```
python3 -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 3. Configure API Key

Create a .env file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the App

```
streamlit run app.py
```

## 📁 File Structure

```
.
├── app.py                # Main Streamlit application
├── .env                  # Your Gemini API key (not committed)
├── requirements.txt      # All dependencies
├── README.md             # This file
└── ...                   # Temp files created at runtime
```

## 🙌 Acknowledgments
- Google GenAI SDK
- Agno - AI Agent Framework
- Streamlit

## 📄 License

MIT License. See LICENSE for details.
