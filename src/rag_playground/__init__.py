import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()


def main():
    # load files
    loaded_files = load_files()

    # chunk files
    chunked_files = chunk_files(loaded_files)
    print(f"docs len: {len(loaded_files)}\nchunks len: {len(chunked_files)}")

    print(f"chunk 0: {chunked_files[0]}\n\n\nchunk 1: {chunked_files[1]}")
    # embed files
    embedded_files = embed_files(chunked_files)

    # store files

    # prompt user for query

    # retrieve documents

    # build context for the llm

    # generate response


def load_files() -> list[Document]:
    return [
        Document(
            page_content=file.read_text(encoding="utf-8"),
            metadata={"source": str(file)},
        )
        for file in Path("docs").glob("*.txt")
    ]


def chunk_files(
    documents: list[Document], chunk_size=1024, chunk_overlap=64
) -> list[Document]:
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    ).split_documents(documents)


def embed_files(chunks: list[Document]):
    ## load embedding model from open ai
    return


if __name__ == "__main__":
    main()
