from langchain.chat_models import ChatOpenAI

def score_response(question, answer):
    prompt = f"""
    Evaluate this candidate's response on a scale of 1 to 10.
    Question: {question}
    Answer: {answer}
    Provide a brief justification.
    """
    llm = ChatOpenAI()
    response = llm.predict(prompt)
    return response
