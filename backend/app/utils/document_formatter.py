from langchain_core.documents import Document


def format_documents(
    docs: list[Document]
) -> str:

    formatted = []

    for doc in docs:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        page = doc.metadata.get(
            "page",
            "-"
        )

        formatted.append(

            f"""
Source: {source}
Page: {page}

{doc.page_content}
"""

        )

    return "\n\n--------------------\n\n".join(
        formatted
    )