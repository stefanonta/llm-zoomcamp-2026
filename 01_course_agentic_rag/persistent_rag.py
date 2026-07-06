from sqlitesearch import TextSearchIndex

# Connecting the database created in ingest_sql.py
with TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    db_path="faqs.db"
) as sqlite_index:

    # Count the number of entries in the index (count() is inherited from TextSearchIndex class of sqlitesearch library)
    print(sqlite_index.count())

    # Trying a search
    # <- list
    search_results = sqlite_index.search("how do i get a certificate?", num_results=5)

    # Print the 5 search results
    for faq in search_results:
        print(f"""{faq["question"]}:\n{faq["answer"]}\n\n""")

# Closing the databse is handled by the 'with' statement, so no need to call db.close() 
