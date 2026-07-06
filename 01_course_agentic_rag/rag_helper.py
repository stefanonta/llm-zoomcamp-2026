# The RAG logic (search, prompt, LLM)

INSTRUCTIONS = """
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
"""

PROMPT_TEMPLATE = """
QUESTION: {user_query}

CONTEXT:
{context}
""".strip()


class RAGbase:
    def __init__(
        self,
        index,  # built by ingest.build_index() or  and will passed at instatiation to the constructor of RAGbase
        llm_client,
        instructions=INSTRUCTIONS,
        prompt_template=PROMPT_TEMPLATE,
        course="llm-zoomcamp",
        llm_model="gpt-5.4-mini-2026-03-17",
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.prompt_template = prompt_template
        self.course = course
        self.llm_model = llm_model

    def search(self, query, n_results=5):
        """
        -> list(dict)
        Search the index for relevant documents based on the query.
        Returns a list of the top_k most relevant documents.
        """
        # Used to filter the search results to only include courses that are relevant to the query
        # Example: "llm-zoomcamp", if you have multiple courses you can filter by course
        filter_dict = {"course": self.course}
        # Boost is used to give more weight to certain fields in the search results
        # Example: "question": 3.0, "section": 0.5 -> question is 3 times more important than section
        boost_dict = {"question": 3.0, "section": 0.5}

        search_results = self.index.search(
            query,
            num_results=n_results,
            filter_dict=filter_dict,
            boost_dict=boost_dict
        )
        return search_results

    def build_context(self, search_results):
        """
        -> str
        Build the context string variable, from the search results, to be included in the prompt
        """
        context_lines = []
        # Iterate over the search_results which is a list(dict) and extract the relevant information to build the context
        for doc in search_results:
            context_lines.append(doc["section"])
            context_lines.append("Q: " + doc["question"])
            context_lines.append("A: " + doc["answer"])
            context_lines.append("")
        # Join the context lines with a newline character into a single string and return it
        context = "\n".join(context_lines).strip()
        # <- str
        return context

    def build_prompt(self, user_query, context):
        """
        -> str
        Build the prompt string variable to be passed to the LLM for generating the answer.
        It combines the instructions, the question and the context into a single string.
        """
        final_prompt = self.prompt_template.format(
            user_query=user_query, context=context
        )
        return final_prompt

    def llm(self, prompt):
        """
        -> str
        Send the prompt and get an answer using the LLM client.
        It sends the prompt to the LLM and retrieves the generated answer.
        """
        message_history = [
            {"role": "developer", "content": INSTRUCTIONS},
            {"role": "user", "content": prompt},
        ]
        response = self.llm_client.responses.create(
            model=self.llm_model, input=message_history
        )

        return response.output_text

    def rag(self, user_query):
        """
        The orchestrator function that combines the search, context building, prompt building
        and LLM response generation to answer the user's query.
        """
        search_result = self.search(user_query)
        prompt = self.build_prompt(user_query, self.build_context(search_result))
        answer = self.llm(prompt)
        return answer
