from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("Please set your OpenAI API key in the .env file.")
    st.stop()

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Streamlit UI
st.header("Chatbot")

# Upload a PDF file
with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file here to start asking questions", type="pdf")

if file:
    # Extract text from PDF
    reader = PdfReader(file)
    text = "".join(page.extract_text() for page in reader.pages)

    # Split text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # Generate embeddings
    embeddings = OpenAIEmbeddings()

    # Create vector store - FAISS (Facebook AI Similarity Search)
    vector_store = FAISS.from_texts(chunks, embeddings)

    # Get User input
    user_question = st.text_input("Enter your question below:")

    if user_question:
        # Perform similarity search
        match = vector_store.similarity_search(user_question)

        # Set up the LLM
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            temperature=0,
            max_tokens=1000,
            model_name="gpt-3.5-turbo"
        )

        # Process the query and provide a response
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=match, question=user_question)

        # Display the response
        st.write(response)
else:
    st.info("Upload a PDF file to begin exploring its content interactively.")
