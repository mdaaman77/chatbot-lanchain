from app.loaders.document_loader import Document

from app.splitters.text_splitter import TextSplitterFactory
from app.vectorstores.pinecone_initializer import PineconeInitializer
from app.vectorstores.pinecone_store import PineconeStore


class IngestService:
    @staticmethod
    def ingest():
        try:
            PineconeInitializer.initialize()
            docs = Document.load_documents()
            splitter = TextSplitterFactory.get_splitter()
            chunks = splitter.split_documents(docs)

            vectorstore =  PineconeStore.get_vector_store()
            response =  vectorstore.add_documents(chunks)
            
            return {
                "documents": len(docs),
                "chunks": len(chunks),
                "id_size": len(response),
                "status": "success"
            }
        except Exception as e:
            return {
                "documents": 0,
                "chunks": 0,
                "status": "error",
                "message": str(e)
            }

