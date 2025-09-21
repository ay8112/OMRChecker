📝 Automated OMR Evaluation & Scoring System
📌 Overview

This project automates the evaluation of OMR sheets using Streamlit and OpenCV.
Instead of manual checking, scanned OMR sheets can be uploaded, processed by the OMRChecker engine, and scored instantly.

✅ Upload OMR sheet images (jpg, jpeg, png)

✅ Auto detect and evaluate answers

✅ Generate per-subject & total scores

✅ Results displayed instantly on a simple web UI

✅ Reduces evaluation from days to minutes

🚀 Features

Image preprocessing (rotation, skew, illumination correction)

Bubble detection & classification

Answer key matching (supports multiple exam versions)

Instant result generation (0–20 per subject, 0–100 total)

Web-based interface for easy use

🛠️ Tech Stack

Python (Core logic)

OpenCV, NumPy, SciPy (Image processing)

Streamlit (Frontend UI)

SQLite/PostgreSQL (Optional result storage)

📂 Project Structure
OMRChecker/
│── omr_engine/        # Core OMR detection and evaluation logic
│── app.py             # Streamlit frontend app (newly added)
│── requirements.txt   # Project dependencies
│── requirements.dev.txt # Dev dependencies (testing/linting)
│── static/            # Static files (if any)
│── templates/         # Templates (optional for Flask version)

⚙️ Installation

Clone the repo

git clone https://github.com/ay8112/OMRChecker.git
cd OMRChecker


Create virtual environment

python -m venv venv


Activate environment

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run Streamlit app

streamlit run app.py

🎯 Usage

Open http://localhost:8501 in your browser.

Upload a scanned OMR sheet.

The system runs evaluation and displays scores.

Results can be exported as needed.

📊 Example Workflow

Student fills OMR sheet → Scanned via phone

Upload sheet in Streamlit UI

System evaluates answers → Generates scores

Evaluator downloads/export results

📜 License

This project is open-source and available under REPO OF ay8112 user

⚡ With this setup, you can deploy on Streamlit Cloud, Hugging Face Spaces, or Render for free.
