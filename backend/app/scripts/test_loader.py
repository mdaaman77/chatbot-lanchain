from app.loaders.document_loader import Document

docs = Document.load_documents()
# print(len(docs))
# print(docs[0].page_content[:500])
# print(docs[0].metadata)

print(docs[1])