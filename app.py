import streamlit as st
from resume_parser import extract_resume_text
from interviewer import generate_question, score_response

st.title("🧠 GenAI Virtual Interviewer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
if uploaded_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())
    resume_text = extract_resume_text("temp_resume.pdf")
    st.subheader("📄 Extracted Resume Content")
    st.text(resume_text)

    if "context" not in st.session_state:
        st.session_state.context = resume_text

    if st.button("Generate Interview Question"):
        question = generate_question(st.session_state.context)
        st.session_state.question = question

    if "question" in st.session_state:
        st.subheader("🤖 Interview Question")
        st.write(st.session_state.question)
        answer = st.text_input("Your Answer:")

        if st.button("Submit Answer"):
            score = score_response(st.session_state.question, answer)
            st.success(f"LLM Score: {score}/10")
