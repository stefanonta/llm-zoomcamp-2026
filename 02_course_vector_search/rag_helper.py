INSTRUCTIONS = '''
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
'''

PROMPT_TEMPLATE = '''
QUESTION: {question}

CONTEXT:
{context}
'''.strip()

SQL_SEARCH_TEMPLATE = '''
SELECT course, section, question, answer
FROM documents
WHERE course = %s
ORDER BY faq_answer_vector <=> %s::vector
LIMIT %s
'''

class RAGBase:

    def __init__(
        self,
        index,
        llm_client,
        instructions=INSTRUCTIONS,
        prompt_template=PROMPT_TEMPLATE,
        course='llm-zoomcamp',
        model='gpt-5.4-mini'
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.course = course
        self.prompt_template = prompt_template
        self.model = model

    def search(self, query, num_results=5):
        boost_dict = {'question': 3.0, 'section': 0.5}
        filter_dict = {'course': self.course}

        return self.index.search(
            query,
            num_results=num_results,
            boost_dict=boost_dict,
            filter_dict=filter_dict
        )

    def build_context(self, search_results):
        lines = []

        for doc in search_results:
            lines.append(doc['section'])
            lines.append('Q: ' + doc['FAQ'])
            lines.append('A: ' + doc['answer'])
            lines.append('')

        return '\n'.join(lines).strip()

    def build_prompt(self, query, search_results):
        context = self.build_context(search_results)
        return self.prompt_template.format(
            question=query, context=context
        )

    def llm(self, prompt):
        input_messages = [
            {'role': 'developer', 'content': self.instructions},
            {'role': 'user', 'content': prompt}
        ]

        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )

        return response.output_text

    def rag_answer(self, query):
        search_results = self.search(query)
        prompt = self.build_prompt(query, search_results)
        answer = self.llm(prompt)
        return answer

class RAGVector(RAGBase):

    def __init__(self, embedder, **kwargs):
        # Run the _init_ method of the parent class
        super().__init__(**kwargs)
        self.embedder = embedder
    
    def search(self, query, num_results=5):
        vector_query = self.embedder.encode(query)
        
        search_results = self.index.search(
            vector_query,
            num_results=num_results,
            filter_dict={'course': self.course}
        )  
        return search_results

class RAGPgVector(RAGBase):
    def __init__(self, embedder, conn, **kwargs):
        # Run the _init_ method of the parent class
        super().__init__(index=None, **kwargs)
        self.embedder = embedder
        self.conn = conn

    def vec_to_str(self, vector):
        """
        This method converts a list of numbers (a vector) into a string formatted
        as per the "pgvector vector" accepted format
        """
        return "[" + ",".join(str(n) for n in vector) + "]"
    
    def run_sql_query(self, sql_query, sql_query_params=None):
        """
        This method runs a read-only (SELECT) SQL query and returns the results.
        If an error is raised, the connection is rolled back and the error is raised again.
        """
        try:
            results = self.conn.execute(sql_query, sql_query_params or ()).fetchall()
        except Exception:
            self.conn.rollback() # "reset" the connection to the state it was in before the query
            raise # raise the initial error (but the connection is now rolled back ready for the next query) 
        return results
        
    def search(self, query, sql_query=SQL_SEARCH_TEMPLATE, num_results=5):
        vector_query = self.embedder.encode(query)
        # Convert the vector to a pgvector-compatible vector-like string
        vector_query_str = self.vec_to_str(vector_query)
        # Run the SQL query to search for the most similar documents
        results = self.run_sql_query(sql_query, (self.course, vector_query_str, num_results))
        formatted_results = [ 
            {"course": row[0], "section": row[1], "FAQ": row[2], "answer": row[3]}
            for row in results
        ]
        return formatted_results