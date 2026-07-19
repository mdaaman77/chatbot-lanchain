from langchain_core.vectorstores import VectorStoreRetriever
from app.vectorstores.pinecone_store import PineconeStore
from app.llms.factory import LLMFactory

class RetrieverFactory:

    @staticmethod
    def get_retriever(k: int = 3) -> VectorStoreRetriever:
        vector_store = PineconeStore.get_vector_store()
        return vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k}
        )

    @staticmethod 
    def get_mmr_retriever(k: int = 3):  # Fixed spelling
        vector_store = PineconeStore.get_vector_store()
        return vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={"k": k}
        )

    @staticmethod
    def get_multiQuery_retriever(k: int = 3):  # Fixed spelling
        vector_store = PineconeStore.get_vector_store()
        base_retriever = vector_store.as_retriever(search_kwargs={"k": k})
        llm = LLMFactory.getLlm("gemini")

        class MultiQueryWrapper:
            def invoke(self, query: str):
                # Expand query using LLM
                prompt = f"Rewrite the query '{query}' into 3 semantically different variants."
                response = llm.invoke(prompt)
                
                # --- FIX: Safe extraction of string text from any response format ---
                raw_content = response.content if hasattr(response, 'content') else response
                
                if isinstance(raw_content, list):
                    extracted_parts = []
                    for part in raw_content:
                        if isinstance(part, str):
                            extracted_parts.append(part)
                        elif isinstance(part, dict) and "text" in part:
                            extracted_parts.append(part["text"])
                        elif hasattr(part, "text"):
                            extracted_parts.append(part.text)
                    response_text = "\n".join(extracted_parts)
                else:
                    response_text = str(raw_content)
                
                # Split variants by newline safely
                variants = [query] + [q.strip() for q in response_text.split("\n") if q.strip()]

                results = []
                for q in variants:
                    docs = base_retriever.invoke(q)
                    results.extend(docs)

                # Deduplicate by doc id
                seen = set()
                merged = []
                for d in results:
                    if d.id not in seen:
                        seen.add(d.id)
                        merged.append(d)
                return merged

        return MultiQueryWrapper()