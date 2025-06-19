from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", temperature=0.2, max_output_tokens=1000)

template = """
You are an expert bank assistant with access to customer data, account information, and banking policies.

Here is relevant banking data from our records: {banking_data}

Here is the customer question: {question}

Instructions:
- Provide accurate information about accounts, transactions, balances, and banking services
- Calculate interest rates, loan payments, and account fees when requested
- Be helpful but maintain banking security and privacy standards
- Only perform calculations if explicitly asked, otherwise retrieve relevant informaton
- For sensitive account information, remind customers to verify their identity if this were a real interaction
- Be professional and clear in your explanations

Answer the customer's question based on the banking data provided.
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def ask_agent(question: str) -> str:
    """
    Ask the banking agent a question and get a response.
    
    Args:
        question (str): The customer's question.
        
    Returns:
        str: The agent's response.
    """
    # Retrieve relevant banking data
    data = retriever.invoke(question)
    
    # Run the chain with the question and retrieved data
    response = chain.invoke({
        "banking_data": data,
        "question": question
    })
    
    return response.content.strip()
