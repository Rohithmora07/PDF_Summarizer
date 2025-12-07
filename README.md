📄 PDF Summarizer

A Streamlit web app that summarizes PDF documents using Grok AI for fast, accurate, and structured summaries.

⭐ Features

📤 Upload any PDF file

🤖 AI-powered summarization using Grok API

📚 Extracts text from all pages using pypdf

⚙️ Simple and clean web UI built with Streamlit

🔐 Secure API key handling with dotenv

🛠️ Tech Stack

Python

Streamlit

Grok API

pypdf

dotenv

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO

2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate the environment

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

🔑 Setup API Key

Create a .env file in the project folder:

GROK_API_KEY=your_api_key_here


Make sure .env is included in .gitignore.

▶️ Run the App
streamlit run App.py

📁 Project Structure
📦 PDF-Summarizer
 ┣ 📜 App.py
 ┣ 📜 requirements.txt
 ┣ 📜 .env (not pushed to GitHub)
 ┗ 📜 README.md

🚀 Deployment (Optional)

You can deploy this app using:

Streamlit Cloud (recommended)

Render

HuggingFace Spaces




📜 License

This project is open-source and free to use.
