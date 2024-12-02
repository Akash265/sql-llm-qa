# Initialize Ollama LLM 
import gradio as gr
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama


# Initialize the database and validate connection
db_path = "sales_database.db"
db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

# Debugging: Validate connection and inspect the database
database_dialect = db.dialect
usable_tables = db.get_usable_table_names()
print("Database dialect:", database_dialect)
print("Usable table names:", usable_tables)

# Define the prompt template
prompt = PromptTemplate(
    template=(
        "You are a highly capable SQL assistant working with a {dialect} database. "
        "Your job is to interact with this database to provide insights from the data. "
        "The database has the following usable tables: {table_info}. "
        "Always use intermediate reasoning steps to ensure the responses are correct and explain your process clearly.\n\n"
        "If the question is ambiguous or lacks specifics, clarify the available options. Do not assume anything."
        "and provide an answer based on the data available. If no relevant data exists, state this clearly and concisely.\n\n"
        "Question: {input}\n"
        "{agent_scratchpad}\n"
        "Final Answer:"
    ),
    input_variables=["dialect", "table_info", "input", "agent_scratchpad"],
)



llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    max_tokens=None,
    timeout=60,
    max_retries=3
    # other params...
)

# Create the SQL agent
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True,
    max_iterations=10,  # Avoid infinite reasoning loops
    early_stopping_method="generate",  # Return partial results if needed
    prompt=prompt,
    agent_type="openai-tools"  # Adjust as needed for Ollama
)

# Define the Gradio app function
def query_database(chatbot_history, user_input):
    """
    Query the SQL database using the LangChain SQL agent.

    Args:
        chatbot_history (list): Chat history containing previous messages.
        user_input (str): The user's natural language query.

    Returns:
        list: Updated chat history with the new user input and agent response.
    """
    try:
        response = agent_executor.invoke({"input": user_input})["output"]
    except Exception as e:
        response = f"An error occurred: {str(e)}"
    
    # Update the chatbot history
    chatbot_history.append((user_input, response))
    return chatbot_history

# Build the Gradio interface
with gr.Blocks() as app:
    gr.Markdown("# SQL Query Chatbot")
    gr.Markdown("Enter your query to interact with the sales database.")
    
    with gr.Row():
        query_input = gr.Textbox(
            label="Your Query",
            placeholder="Ask something like 'What is the sales distribution across different countries?'"
        )
        submit_btn = gr.Button("Submit")
    
    chatbot = gr.Chatbot(label="Chat History")
    clear_btn = gr.Button("Clear History")
    
    # Initialize the chatbot history
    chatbot_history = gr.State([])

    # Set up interactions
    submit_btn.click(
        fn=query_database,
        inputs=[chatbot_history, query_input],
        outputs=[chatbot]
    )
    
    clear_btn.click(
        fn=lambda: [],
        inputs=None,
        outputs=[chatbot]
    )

if __name__ == "__main__":
    app.launch()

