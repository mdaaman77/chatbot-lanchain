from app.chains.rag_chain import RAGChain

from app.utils.response_cleaner import clean_response



class ChatService:


    @staticmethod
    async def chat(
        question: str,
        history: list,
        provider: str,
    ):

        try:


            rag = RAGChain.build(
                provider
            )


            chain = rag["chain"]



            clean_history = [
                h
                for h in history
                if h.strip()
            ]



            response = await chain.ainvoke(
                {
                    "question": question,
                    "history": clean_history,
                }
            )



            cleaned_answer = clean_response(
                response
            )



            return {

                "answer": cleaned_answer,

                "citations": rag["get_sources"]()

            }



        except Exception as e:

            raise RuntimeError(
                f"Chat failed: {str(e)}"
            )