from app.loaders.document_loader import Document

from app.splitters.text_splitter import TextSplitterFactory

from app.vectorstores.pinecone_store import PineconeStore


docs = Document.load_documents()
splitter = TextSplitterFactory.get_splitter()
chunks = splitter.split_documents(docs)

vectorstore =  PineconeStore.get_vector_store()
response = vectorstore.add_documents(chunks)
print(len(response))

