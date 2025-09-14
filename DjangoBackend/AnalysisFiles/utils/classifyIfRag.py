from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config

# Load keys from environment variables
google_api_key = config('GOOGLE_API_KEY')

# Initialize Gemini client
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=google_api_key,
    temperature=0
)

# Define the prompt template
classification_prompt = '''
    You are an expert legal assistant specializing in determining the complexity of legal queries. Your task is to classify whether a query requires retrieval-augmented generation (RAG). Use the following rules:

    - **Basic Query (Send 2):** If the query is simple, factual, or can be answered using common legal knowledge or pre-stored rules within the model's context, respond with 2.
        - Example: "What is the definition of negligence?" → Send 2.
        - Example: "Explain the term 'res judicata.'" → Send 2.

    - **Complex Query (Send 1):** If the query requires searching through external databases or case law to provide a specific or nuanced answer, respond with 1.
        - Example: "What are the key differences between Smith v. Jones (2015) and Brown v. Taylor (2020)?" → Send 1.
        - Example: "Provide examples of how 'negligence' has been interpreted in recent case laws." → Send 1.

    Respond with only the number **1** or **2**. Do not include any explanation or additional text.

    Query:'''

def classify_query(user_prompt):
    try:
        # Create the full prompt
        full_prompt = classification_prompt + user_prompt

        # Make the API call to Gemini
        response = llm.invoke(full_prompt)
        
        # Extract and clean the classification result
        classification_result = response.content.strip()
        print(classification_result)

        # Validate result
        if classification_result not in {"1", "2"}:
            raise ValueError(f"Unexpected classification result: {classification_result}")

        return classification_result

    except Exception as e:
        # Handle errors and provide fallback
        print(f"Error during classification: {e}")
        return "2"