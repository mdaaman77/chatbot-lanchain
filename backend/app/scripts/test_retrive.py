from app.retrievers.retriever import RetrieverFactory
from app.utils.document_formatter import format_documents

# Initialize the retrievers (matching corrected factory names)
sim = RetrieverFactory.get_retriever(k=5)
mmr = RetrieverFactory.get_mmr_retriever(k=10)
multi = RetrieverFactory.get_multiQuery_retriever(k=5)

query = "what is leave policy"
results = []

# Call each retriever’s invoke method
results.extend(sim.invoke(query))
results.extend(mmr.invoke(query))
results.extend(multi.invoke(query))

# Deduplicate documents by their ID
seen = set()
merged = []
for d in results:
      key = d.page_content.strip()
      if key not in seen:
          seen.add(key)
          merged.append(d)

# Format into context string
formatted = format_documents(merged)

print("\n===== Injected Context =====\n")
print(formatted)
print("\n============================\n")