import os
from flask import Flask, render_template, request
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
import ollama
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

embedding_model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

chroma_client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="pdf_data"
)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():

    pdf = request.files['pdf']

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        pdf.filename
    )

    # Save PDF
    pdf.save(filepath)

    # Read PDF
    reader = PdfReader(filepath)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    # Create embeddings
    embeddings = embedding_model.encode(chunks)

    # Clear old data
    existing_ids = collection.get()['ids']

    if existing_ids:
        collection.delete(ids=existing_ids)

    # Store new chunks
    for i, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            ids=[str(i)]
        )

    print("Stored in ChromaDB")

    return "PDF Processed Successfully"


@app.route('/ask', methods=['POST'])
def ask():

    question = request.form['question']

    query_embedding = embedding_model.encode(
        [question]
    )

    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    context = results['documents'][0]

    prompt = f"""
    Answer using this context:

    {context}

    Question:
    {question}
    """

    response = ollama.chat(
        model='mistral',

        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    answer = response['message']['content']

    return answer


if __name__ == '__main__':
    app.run(debug=True)
