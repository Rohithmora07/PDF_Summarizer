# App.py - PDF Summarizer using Groq (free + blazing fast)

import streamlit as st
from pypdf import PdfReader
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("Put your Groq key in .env → GROQ_API_KEY=...")
    st.stop()

client = Groq(api_key=api_key)
# === BEAUTIFUL CUSTOM CSS (2025 edition) ===
st.markdown("""
<style>
/* ------------------------------ */
/* 🌌 APP BACKGROUND & BASE STYLE */
/* ------------------------------ */
.stApp {
    background: radial-gradient(circle at top, #1f1f2e, #141421, #0f0f17);
    font-family: 'Inter', sans-serif;
    color: #e8e8f0;
}

/* ------------------------------ */
/* ✨ TITLE & SUBTITLE            */
/* ------------------------------ */
h1 {
    font-size: 3rem !important;
    font-weight: 900 !important;
    background: linear-gradient(90deg, #8ab4ff, #c084fc, #ff99c8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    letter-spacing: 1px;
}

.subtitle {
    text-align: center;
    font-size: 1.25rem;
    color: #b3b3cc;
    margin-bottom: 40px;
}


/* 🎨 MAIN FILE UPLOAD BOX */
[data-testid="stFileUploader-dropzone"] {
    background: rgba(255, 60, 150, 0.20) !important; /* Change this to any color */
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 14px !important;
    padding: 20px !important;
    transition: 0.3s ease;
}

/* Hover effect (optional) */
[data-testid="stFileUploader-dropzone"]:hover {
    background: rgba(255, 255, 255, 0.12) !important;
    transform: scale(1.01);
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.15);
}


/* ------------------------------ */
/* 🔘 BUTTON - Modern Neo-Glow     */
/* ------------------------------ */
.stButton > button {
    background: linear-gradient(135deg, #6366f1, #a855f7);
    color: white;
    border: none;
    border-radius: 12px;
    height: 48px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.45);
    transition: 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 35px rgba(168, 85, 247, 0.55);
}


/* ------------------------------ */
/* 📄 SUMMARY BOX (Glass Card)     */
/* ------------------------------ */
.summary-card {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(18px);
    padding: 30px;
    border-radius: 20px;
    margin-top: 25px;
    box-shadow: 0 0 25px rgba(0,0,0,0.35);
    color: #e5e5ec;
    font-size: 1.15rem;
    line-height: 1.75;
}


/* ------------------------------ */
/* 🔔 SUCCESS AND INFO MESSAGES   */
/* ------------------------------ */
.stSuccess, .stInfo {
    background: rgba(100, 255, 100, 0.08) !important;
    color: #d1ffd1 !important;
    border-radius: 12px !important;
    border: 1px solid rgba(150, 255, 150, 0.2) !important;
    backdrop-filter: blur(12px);
    padding: 10px;
}


/* ------------------------------ */
/* ⚫ FOOTER                      */
/* ------------------------------ */
.footer {
    text-align: center;
    margin-top: 60px;
    font-size: 0.9rem;
    color: rgba(200, 200, 220, 0.65);
}
</style>

""", unsafe_allow_html=True)

# Optional subtitle
st.markdown("<p class='subtitle'>Powered by Groq • Llama-3.1-70B • Lightning Fast & Free</p>", unsafe_allow_html=True)
st.set_page_config(page_title="PDF Summarizer", page_icon="PDF", layout="centered")
st.title("PDF Summarizer – Groq (Free & Ultra-Fast)")

uploaded = st.file_uploader("Upload PDF", type="pdf")
if uploaded:
    reader = PdfReader(uploaded)
    text = ""
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text += t + "\n"

    if not text.strip():
        st.error("No text found (scanned PDF?)")
    else:
        st.success(f"Extracted {len(text):,} chars from {len(reader.pages)} pages")
        style = st.radio("Style", ["Short", "Medium", "Detailed with bullets"], horizontal=True)

        if st.button("Summarize", type="primary"):
            with st.spinner("Groq is thinking..."):
                prompt = "Summarize concisely." if style == "Short" else \
                         "Summarize clearly." if style == "Medium" else \
                         "Give a detailed summary using bullet points."

                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": f"{prompt}\n\n{text}"}],
                    model="llama-3.3-70b-versatile",      # or "mixtral-8x7b-32768"
                    temperature=0.3,
                    max_tokens=2048
                )
                summary = chat_completion.choices[0].message.content
                st.markdown("### Summary")
                st.markdown(summary)