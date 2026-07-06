# Helper functions to retrieve knowledge base and build a searchable Index object
import requests
from minsearch import Index


def retrieve_faq_data():
    docs_url = "https://datatalks.club/faq/json/courses.json"
    response = requests.get(docs_url)
    # Returns the list of courses with their relative endpoint
    # <- dict or list
    courses_raw = response.json()

    url_prefix = "https://datatalks.club/faq"
    faqs = []
    for course in courses_raw:
        course_url = url_prefix + course["path"]
        # Send get request to retrieve the FAQ for the current course
        response = requests.get(course_url)
        # If HTTP error raise error and stop the execution
        response.raise_for_status()
        # If the request is successful, parse the JSON response and extract the FAQ data
        # <- list(dict)
        faq_data = response.json()
        # Unpack each FAQ entry and append it to the documents list
        faqs.extend(faq_data)

    # <- list(dict)
    return faqs


def build_index(faqs):
    """
    -> list(dict)
    Builds a search index from a list of dictionaries.
    It uses the minsearch library to create a full (reverse) index of the FAQ entries.
    """
    # Instatiate the Index object and set the parament for creating the index
    index = Index(
        keyword_fields=["course"],
        text_fields=["question", "section", "answer"]
    )
    # fit the index which means mapping each documents to the tokenized text_fields
    index.fit(faqs)
    # <- Index
    return index
