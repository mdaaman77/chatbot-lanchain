from operator import itemgetter

from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from app.prompts.rag_prompt import RAG_PROMPT
from app.retrievers.retriever import RetrieverFactory
from app.utils.document_formatter import format_documents
from app.llms.factory import LLMFactory


class RAGChain:

    @staticmethod
    def build(provider: str):

        llm = LLMFactory.getLlm(provider)

        # Store citation filenames
        sources = []


        sim = RetrieverFactory.get_retriever(k=5)
        mmr = RetrieverFactory.get_mmr_retriever(k=10)
        multi = RetrieverFactory.get_multiQuery_retriever(k=5)



        def merge_results(inputs: dict):

            nonlocal sources


            query = inputs["question"]

            history = inputs.get(
                "history",
                []
            )


            results = []


            results.extend(
                sim.invoke(query)
            )

            results.extend(
                mmr.invoke(query)
            )

            results.extend(
                multi.invoke(query)
            )



            # Remove duplicate chunks
            seen = set()

            merged = []


            for doc in results:

                key = doc.page_content.strip()


                if key not in seen:

                    seen.add(key)

                    merged.append(doc)



            # -----------------------------
            # Create unique file citations
            # -----------------------------

            unique_files = set()

            sources = []


            for doc in merged:

                source = doc.metadata.get(
                    "source",
                    "Unknown"
                )


                # Windows path cleanup
                filename = source.split("\\")[-1]


                if filename not in unique_files:

                    unique_files.add(filename)


                    sources.append(
                        {
                            "source": filename
                        }
                    )



            formatted = format_documents(
                merged
            )


            history_text = (
                "\n".join(history)
                if history
                else ""
            )



            print(
                "\n===== Injected Context =====\n"
            )


            print(
                formatted
                + "\n\nConversation history:\n"
                + history_text
            )


            print(
                "\n============================\n"
            )



            return (
                formatted
                + "\n\nConversation history:\n"
                + history_text
            )




        def log_prompt(inputs: dict):

            rendered = RAG_PROMPT.format(
                context=inputs["context"],
                question=inputs["question"],
                history=inputs["history"]
            )


            print(
                "\n===== Final Rendered Prompt =====\n"
            )

            print(rendered)


            print(
                "\n=================================\n"
            )


            return inputs




        chain = (

            {
                "context": RunnableLambda(
                    merge_results
                ),

                "question": itemgetter(
                    "question"
                ),

                "history": itemgetter(
                    "history"
                ),

            }

            | RunnableLambda(
                log_prompt
            )

            | RAG_PROMPT

            | llm

            | StrOutputParser()

        )



        return {

            "chain": chain,

            "get_sources": lambda: sources

        }