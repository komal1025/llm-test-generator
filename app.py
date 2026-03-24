import streamlit as st
from generator import generate_test_cases
from log_analyzer import analyze_logs

st.title("AI Test Case Generator (LLM Powered)")

tab1, tab2 = st.tabs(["Test Case Generator", "Log Analyzer"])

with tab1:
    req = st.text_area("Enter Requirement")
    if st.button("Generate Test Cases"):
        result = generate_test_cases(req)
        st.json(result)

with tab2:
    logs = st.text_area("Paste Logs")
    if st.button("Analyze Logs"):
        result = analyze_logs(logs)
        st.write(result)