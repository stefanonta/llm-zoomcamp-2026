# Ingestion process - it fetches data and writes it to a persistent index one by one with a small delay (to simulate slow ingestion)
from ingest import retrieve_faq_data

faqs = retrieve_faq_data()
print(f"Loaded {len(faqs)} FAQs")

# Filtering for llm-zoomcamp only
faqs_llm_zoomcamp = [faq for faq in faqs if faq["course"] == "llm-zoomcamp"]
print(f"Filtered for llm-zoomcamp: {len(faqs_llm_zoomcamp)} FAQs")

# Creating the sqlitesearch persistent db and adding the faqs to it
import time
from sqlitesearch import TextSearchIndex

with TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    db_path="faqs.db"
) as db:
    for faq in faqs_llm_zoomcamp:
        db.add(faq)
        print(f"""Added to db: {faq["question"]}...""")
        time.sleep(0.1)

# Closing the databse is handled by the 'with' statement, so no need to call db.close() 
# db.close()
print("Completed. Index saved to faqs.db")