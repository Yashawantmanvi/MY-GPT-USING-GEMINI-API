import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        st.error(f"Failed to configure Google API: {e}")
else:
    st.error("Google API key not found. Please set the GOOGLE_API_KEY in the .env file.")

# Function to extract text from PDF files
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to split text into chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100000, chunk_overlap=10000)
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create and save vector store using FAISS
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Function to load conversational chain for QA
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details. If the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer.\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Function to handle user input and generate response
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain.invoke({"input_documents": docs, "question": user_question})
    return response["output_text"]

# Main function to run the Streamlit application
def main():
    st.set_page_config(page_title="Chat with PDF using MY GPT 💁", page_icon="📄", layout="wide")
    st.title("Chat with PDF using MY GPT ")

    # Custom CSS for styling
    st.markdown(
        """
        <style>
            body {
                background-color: #fce4ec; /* Light pink background color for body */
                color: #000000; /* Text color */
            }
            .stApp {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            .sidebar .sidebar-content {
                background-color: #ffffff; /* White background for sidebar */
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                color: #000000; /* Text color for sidebar */
            }
            .sidebar .sidebar-content h3 {
                font-size: 1.5rem;
                margin-bottom: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar
    with st.sidebar:
        st.title("Menu")
        pdf_docs = st.file_uploader("Upload PDF Files", accept_multiple_files=True)
        if st.button("Submit & Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    try:
                        raw_text = get_pdf_text(pdf_docs)
                        text_chunks = get_text_chunks(raw_text)
                        get_vector_store(text_chunks)
                        st.success("PDFs processed successfully.")
                    except Exception as e:
                        st.error(f"An error occurred while processing PDFs: {e}")

    # Dark mode toggle for sidebar
    dark_mode_sidebar = st.sidebar.checkbox("Dark Mode")

    # Conditionally apply dark mode to whole page if toggle is enabled
    if dark_mode_sidebar:
        st.markdown(
            """
            <style>
                body {
                    background-color: #333333; /* Dark background color for body */
                    color: #ffffff; /* Text color */
                }
                .sidebar .sidebar-content {
                    background-color: #574b90; /* Dark lavender cream color for sidebar */
                    color: #ffffff; /* Text color for sidebar */
                }
            </style>
            """,
            unsafe_allow_html=True
        )

    # Main content area
    st.write("### Ask a Question from the PDF Files")
    user_question = st.text_input("Type your question here")

    if user_question:
        st.write("### Your Question:")
        st.write(user_question)

        st.write("### Response:")
        if pdf_docs:
            try:
                response = user_input(user_question)
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred while generating a response: {e}")

if __name__ == "__main__":
    main()
