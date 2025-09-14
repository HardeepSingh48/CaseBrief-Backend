from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config

# Load keys from environment variables
google_api_key = config('GOOGLE_API_KEY')

# Initialize the Gemini client
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=google_api_key,
    temperature=0
)

def get_standalone_question(chat_history, user_input):
    """
    Function to get a standalone question from chat history and user input using Gemini.

    Args:
        chat_history (list): List of dictionaries containing chat history.
        user_input (str): User's current question.

    Returns:
        str: Reformulated standalone question.
    """
    # Format chat history into a prompt
    chat_history_formatted = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history])

    # Define the prompt
    prompt = f"""
    Given the following chat history and the latest user question, reformulate the question into a standalone question that can be understood without the context of the chat history. 
    Do not answer the question, just reformulate it and return only the reformulated question.

    Chat History:
    {chat_history_formatted}

    User Question:
    {user_input}
    """

    try:
        # Make the API call to Gemini
        response = llm.invoke(prompt)
        
        # Extract and return the reformulated question
        standalone_question = response.content.strip()
        return standalone_question
        
    except Exception as e:
        print(f"Error getting standalone question: {e}")
        # Fallback: return the original user input
        return user_input

# Main function for testing
if __name__ == "__main__":
    chat_history = [
        {"role": "user", "content": "Tell me about Vodafone vs Union of India case."},
        {"role": "assistant", "content": "Vodafone is an amazing company"},
    ]

    user_input = "How is it similar to ASTRAZENECA AB & ANR. VS. INTAS PHARMACEUTICALS LIMITED"
    standalone_question = get_standalone_question(chat_history, user_input)
    print("Standalone Question:", standalone_question)