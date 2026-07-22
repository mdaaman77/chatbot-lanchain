from app.loaders.document_loader import Document

from app.splitters.text_splitter import TextSplitterFactory
from app.vectorstores.pinecone_initializer import PineconeInitializer
from app.vectorstores.pinecone_store import PineconeStore
from app.keyword_search.bm25_index import BM25Index
from app.keyword_search.bm25_store import BM25Store


class IngestService:
    @staticmethod
    def ingest():
        try:
            PineconeInitializer.initialize()
            docs = Document.load_documents()
            splitter = TextSplitterFactory.get_splitter()
            chunks = splitter.split_documents(docs)

            vectorstore =  PineconeStore.get_vector_store()
            response_vectorStore =  vectorstore.add_documents(chunks)

            bm25 =  BM25Index.build(chunks)
           
            
            
            return {
                "documents": len(docs),
                "chunks": len(chunks),
                "id_size _vs": len(response_vectorStore),
                "status": "success"
            }
        except Exception as e:
            return {
                "documents": 0,
                "chunks": 0,
                "status": "error",
                "message": str(e)
            }

