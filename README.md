# Testimonial App Package

Contents:
- testimonial_app.py         (original PyQt5 desktop application — UNCHANGED)
- streamlit_app.py           (helper Streamlit wrapper for distribution & download)
- requirements.txt           (Python packages required)
- README.md                  (this file)

Notes:
- You asked that the original code remain the same. The file `testimonial_app.py` is included verbatim.
- The original file creates a PyQt5 native desktop GUI; it is not a Streamlit web application.
- `streamlit_app.py` is provided as a wrapper so you can host a small Streamlit page that allows downloading the original file and shows instructions.

To run locally:
1. Create and activate a virtual environment.
2. Install requirements: `pip install -r requirements.txt`
3. To run the PyQt desktop app: `python testimonial_app.py`
4. To run the Streamlit wrapper (optional): `streamlit run streamlit_app.py`

If you'd like, I can:
- Convert the app into a real Streamlit web application (this will modify the original logic and UI).
- Or keep the original desktop behavior but create a web API to generate PDFs (also requires code changes).

Reply which option you prefer if you want a web-deployable app.
