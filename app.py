# GitHub Copilot Instruction:
"""
Create a Streamlit app that does the following:

1. Set page title to "OMR Checker" and icon to 📝
2. Display title: "Automated OMR Checker"
3. Display text: "Upload your scanned OMR sheets and get evaluated instantly."
4. Add a file uploader to accept jpg, jpeg, png files
5. When a file is uploaded:
   - Save the uploaded file temporarily as "temp.jpg"
   - Run the existing OMRChecker engine script:
     python omr_engine/scan.py temp.jpg > result.txt
   - Read "result.txt" and display its contents in Streamlit
6. Ensure the app layout is wide
7. Make sure it works locally when running `streamlit run app.py`
"""

import streamlit as st
import os

st.set_page_config(page_title="OMR Checker", page_icon="📝", layout="wide")

st.title("📝 Automated OMR Checker")
st.write("Upload your scanned OMR sheets and get evaluated instantly.")

uploaded_file = st.file_uploader("Upload OMR Sheet", type=["jpg","jpeg","png"])

if uploaded_file:
    with open("temp.jpg","wb") as f:
        f.write(uploaded_file.read())
    os.system("python omr_engine/scan.py temp.jpg > result.txt")
    with open("result.txt","r") as f:
        st.text(f.read())
