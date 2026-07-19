from langchain_core.prompts import ChatPromptTemplate,PromptTemplate,MessagesPlaceholder



RAG_PROMPT = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are an AI assistant.

Answer ONLY using the supplied context.

If the answer cannot be found in the context , only stick to the content do not share othere information apart from content
reply with:

"I couldn't find that information in the provided documents."

Do not hallucinate.

Always answer in Markdown.

Context:

{context}

"""
        ),

        MessagesPlaceholder(
            variable_name="history"
        ),

        (

            "human",

            "{question}"

        )

    ],
)