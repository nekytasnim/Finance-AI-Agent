from uuid import uuid4
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
import os
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

config = {"use_llm": True,
          "gemini_api_key": os.getenv("GOOGLE_API_KEY")}

converter = PdfConverter(
    artifact_dict=create_model_dict(),
    config=config
)
rendered_pdf = converter("batch1-0483.pdf")
doc_text, _, _ = text_from_rendered(rendered_pdf)

rendered_image = converter('batch1-0484.jpg')
image_text, _, _ = text_from_rendered(rendered_image)

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain_db"
doc_1 = Document(page_content=doc_text, id=1)
doc_2 = Document(page_content=image_text, id=2)
documents = [doc_1, doc_2]
uuids = [str(uuid4()) for _ in range(len(documents))]

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings
)

vector_store.add_documents(documents=documents, ids=uuids)

retriever = vector_store.as_retriever(search_type="mmr")
