from app.chains.rag_chain import RAGChain

from app.utils.response_cleaner import clean_response
from app.memory.conversation_manager import ConversationManager



class ChatService:


    @staticmethod
    async def chat(
        question: str,
        session_id: str,
        provider: str,
    ):

        try:

            history = await ConversationManager.get_message(session_id=session_id)
            
            rag_chain_instance = RAGChain()
            chain = rag_chain_instance.build(provider, history)


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

            ConversationManager.add_message(session_id=session_id,question={"role ":"user",
                                                                            "message":question})
            
            ConversationManager.add_message(session_id=session_id,question={"role ":"assistant",
                                                                                        "message":question})
            
            


            return {

                "answer": cleaned_answer,

                "citations": rag["get_sources"]()

            }



        except Exception as e:

            raise RuntimeError(
                f"Chat failed: {str(e)}"
            )