import environ
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

API_KEY = env('OPENAI_API_KEY')

# Setup database
db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://postgres:{env('DBPASS')}@localhost:5432/{env('DATABASE')}",
)

# Setup llm
llm = OpenAI(temperature=0, openai_api_key=API_KEY)

# Create db chain
QUERY = """
Imagine you are having a conversation with a database expert. You ask a question, and they respond by first writing a correct SQL query, then running it, and finally explaining the results in a friendly manner.
Use this format:

You: [Your question here]
Expert: Sure, let me find that out for you.
Expert: [SQL Query]
Expert: Here are the results: [SQL Result]
Expert: [Answer]

You: {question}
"""

# Setup the database chain
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)


def get_prompt():
    print("Type 'exit' to quit")

    while True:
        prompt = input("Enter a prompt: ")

        if prompt.lower() == 'exit':
            print('Exiting...')
            break
        else:
            try:
                question = QUERY.format(question=prompt)
                print(db_chain.run(question))
            except Exception as e:
                print(e)

get_prompt()
