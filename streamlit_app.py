# streamlit_app.py
"""
Streamlit wrapper (keeps the original testimonial_app.py unchanged).
This wrapper does NOT convert the PyQt5 app into a Streamlit UI.
It provides:
 - A preview of the original file contents.
 - A download link for the original testimonial_app.py
 - Requirements and README display.

Why: You asked to keep the code exactly the same. Converting PyQt5 desktop UI to a web UI requires changing the logic.
If you want a full web conversion (Streamlit-based form and PDF generation), I can do that next (it will modify code).
"""

import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Testimonial App Package", layout="wide")

st.title("Testimonial App — Packaging (original code kept unchanged)")
st.markdown(
    """
This package contains your original `testimonial_app.py` (kept exactly as provided) plus helpful files:
- `requirements.txt` — Python packages you need.
- `README.md` — Instructions to run locally.
- `streamlit_app.py` — This helper wrapper (does **not** alter the original file).

**Important note:** The original file is a PyQt5 desktop application. Running it on a typical Streamlit hosting service is not appropriate because PyQt5 creates a native desktop GUI.
If you want a **true web app**, I can convert the logic into a Streamlit app (this will change the code). Let me know and I'll produce a web-converted version.
"""
)

st.header("Files inside the package")
st.write("- testimonial_app.py (original, unchanged)")
st.write("- streamlit_app.py (this file)")
st.write("- requirements.txt")
st.write("- README.md")

st.header("Preview of testimonial_app.py (first 400 lines)")
path = Path("testimonial_app.py")
if path.exists():
    txt = path.read_text()
    st.code("\n".join(txt.splitlines()[:400]), language="python")
else:
    st.info("Original file not present in this runtime. In the distributed zip it will be included.")

st.header("How to use this package (local desktop)")
st.markdown(
    """
1. Create a virtual environment: `python -m venv venv`  
2. Activate it: Windows: `venv\\Scripts\\activate`, macOS/Linux: `source venv/bin/activate`  
3. Install requirements: `pip install -r requirements.txt`  
4. Run the app (desktop): `python testimonial_app.py`  

If you want a **Streamlit web version**, reply here and I will convert the logic into a proper Streamlit app (this will require code changes).
"""
)

st.header("Download files")
with open("testimonial_app.py", "rb") as f:
    data = f.read()
st.download_button("Download original testimonial_app.py", data=data, file_name="testimonial_app.py")

with open("requirements.txt", "rb") as f:
    data2 = f.read()
st.download_button("Download requirements.txt", data=data2, file_name="requirements.txt")

with open("README.md", "rb") as f:
    data3 = f.read()
st.download_button("Download README.md", data=data3, file_name="README.md")
