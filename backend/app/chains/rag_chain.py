from typing import List
from langchain_core.runnables import RunnableLambda, RunnablePassthrough,RunnableBranch
from langchain_core.output_parsers import StrOutputParser

from app.prompts.rag_prompt import RAG_PROMPT
from app.utils.document_formatter import format_documents
from app.llms.factory import LLMFactory
from app.retrievers.hybrid_retriever import HybridRetriever
from app.re_ranking.crossEncoder import CrossEncoder
from app.memory.conversation_manager import ChatMessage
#
from app.evaluate_chunks.evalutate import EvaluateChunks


class RAGChain:

    def __init__(self):
        self.hybrid_retriever = HybridRetriever().retrieve()
        self.re_ranker = CrossEncoder().rerank()
        self.str_output_parser = StrOutputParser()
        self.evaluator = EvaluateChunks(threshold=0.5)

    def build(self, provider: str, history: List[ChatMessage]):
        llm = LLMFactory(provider)

        # 1. Fetch filtered docs
        retrieval_chain = (
            self.hybrid_retriever 
            | self.re_ranker 
            | RunnableLambda(self.evaluator.pass_threshold)
        )

        # 2. Define the LLM Branch (Only executes if docs exist)
        llm_branch = (
            {
                "context": lambda x: format_documents(x["docs"]),
                "history": lambda _: history,
                "question": lambda x: x["question"]
            }
            | RAG_PROMPT
            | llm
            | self.str_output_parser
        )

        # 3. Branching logic
        chain = (
            {
                "docs": retrieval_chain,
                "question": RunnablePassthrough()
            }
            | RunnableBranch(
                
                (lambda x: len(x["docs"]) == 0, RunnableLambda(lambda _: "I couldn't find relevant information in the provided documents.")),
                
                llm_branch
            )
        )

        return chain
