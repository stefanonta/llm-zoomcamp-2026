from sqlitesearch import TextSearchIndex
from ingest import build_index, retrieve_faq_data
from rag_helper import RAGbase
from dotenv import load_dotenv
from openai import OpenAI


def main():
    # load_dotenv()  # Read the .env file and set environment variables
    load_dotenv()
    # Retrieve the knowledge base and build a searchable Index object
    knwoledge_base = retrieve_faq_data()
    # Uncomment to use minsearch to build a volatile index                                
    # searchable_index = build_index(knwoledge_base)

    # Using persistent sqlite index
    index = TextSearchIndex(
        text_fields=["question", "section", "answer"],
        keyword_fields=["course"],
        db_path="faqs.db"
    )
    llm_client = OpenAI()
    website_assistant = RAGbase(index, llm_client)

    answer = website_assistant.rag("I just discovered the course. Can I join now?")
    print(answer,"\n")

    answer2 = website_assistant.rag("How do I get a certificate?")
    print(answer2, "\n")

    answer3 = website_assistant.rag("Do we learn python in the course?")
    print(answer3, "\n")


# ====================================================================================================
if __name__ == "__main__":
    main()
