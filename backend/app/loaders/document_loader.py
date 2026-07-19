from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    TextLoader,
)
import os


class Document:
    @staticmethod
    def load_documents():
        base_dir = os.path.dirname(os.path.dirname(__file__))  # goes up from scripts/
        docs_path = os.path.join(base_dir, "documents")

        pdf_loader = DirectoryLoader(
            docs_path,
            glob="**/*.pdf",
            loader_cls=PyPDFLoader,
        )

        markdown_loader = DirectoryLoader(
            docs_path,
            glob="**/*.md",
            loader_cls=TextLoader,
        )

        documents = []
        documents.extend(pdf_loader.load())
        documents.extend(markdown_loader.load())
        return documents
