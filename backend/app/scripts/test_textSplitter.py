from app.loaders.document_loader import Document
from app.splitters.text_splitter import TextSplitterFactory

docs = Document.load_documents()
splitter = TextSplitterFactory.get_splitter()

chunks = splitter.split_documents(docs)

print(len(chunks), "\n")

# Print each chunk's text on a new line
for c in chunks:
    print(c.page_content)   # print the text of the chunk
    print("\n")             # add a blank line between chunks
