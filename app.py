import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Interview Dashboard", layout="wide")

COL_NAME = "Name"
COL_VERTICAL = "Vertical(s) Preferences (Any 3)"
COL_REASON = "Why do you wish to join us?"
COL_EXPERIENCE = "Mention your past experiences."
COL_DONE = "Interview Done"

def ensure_done_column(df: pd.DataFrame):
    if COL_DONE not in df.columns:
        df[COL_DONE] = "No"
    else:
        df[COL_DONE] = df[COL_DONE].fillna("No")
        df[COL_DONE] = df[COL_DONE].apply(lambda x: "Yes" if str(x).lower() == "yes" else "No")
    return df

def load_excel(uploaded_file):
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    return ensure_done_column(df)

def save_excel(df):
    buffer = BytesIO()
    df.to_excel(buffer, index=False, engine="openpyxl")
    buffer.seek(0)
    return buffer

st.title("📋 Interview Dashboard")
st.write("Upload the Excel sheet and mark each interview as completed using **Yes/No**.")

uploaded = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded:
    df = load_excel(uploaded)

    st.sidebar.header("Select Candidate")
    names = df[COL_NAME].tolist()
    selected = st.sidebar.selectbox("Candidate", names)

    row = df[df[COL_NAME] == selected].iloc[0]

    st.subheader(f"Interviewee: {row[COL_NAME]}")
    st.write("### Vertical Preferences")
    st.write(row[COL_VERTICAL])

    st.write("### Why do you wish to join us?")
    st.write(row[COL_REASON])

    st.write("### Past Experiences")
    st.write(row[COL_EXPERIENCE])

    st.write("### Interview Status")
    current_status = row[COL_DONE]
    new_status = st.radio(
        "Interview Done?",
        options=["Yes", "No"],
        index=0 if current_status == "Yes" else 1,
        horizontal=True
    )

    df.loc[df[COL_NAME] == selected, COL_DONE] = new_status

    st.success("Status updated (not saved yet).")

    st.write("---")
    st.write("### Save Updated File")
    st.download_button(
        label="Download Updated Excel",
        data=save_excel(df),
        file_name="updated_interview_list.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
