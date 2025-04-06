from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def load_rag_chain(vector_index):
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    retriever = FAISS.load_local(vector_index, OpenAIEmbeddings()).as_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa
