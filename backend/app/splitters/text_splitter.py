from langchain_text_splitters  import RecursiveCharacterTextSplitter



class TextSplitterFactory:

    @staticmethod 
    def get_splitter():
       return RecursiveCharacterTextSplitter(

            chunk_size=1000,

            chunk_overlap=200,

            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ]
        )