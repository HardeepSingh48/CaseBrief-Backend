from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config
import json

# Load keys from environment variables
google_api_key = config('GOOGLE_API_KEY')

# Initialize Gemini client
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=google_api_key,
    temperature=0
)

def extract_search_terms(user_prompt):
    # Define the prompt template
    prompt = f'''
    Analyze the input to extract relevant search terms for a query. This system is a database of legal cases that uses string matching. The database will never contain words like 'highlights,' 'summary,' or 'details.' Focus only on the core search terms related to the input. If the input contains a year, generate a date range in the format 'fromdate=1-1-[year] todate=31-12-[year]'. Output the result in JSON format with the key search_query. Examples:
    Input: vodafone vs union of India
    Output: {{"search_query": "vodafone vs union of India"}}

    Input: vodafone vs union of India (2018)
    Output: {{"search_query": "vodafone vs union of India fromdate: 1-1-2018 todate: 31-12-2018"}}

    Input: supreme court ruling on privacy (2017)
    Output: {{"search_query": "supreme court ruling on privacy fromdate: 1-1-2017 todate: 31-12-2017"}}

    Input: give me highlights of all cases of zomato in the year 2015 and tell me the verdicts
    Output: {{"search_query": "zomato fromdate: 1-1-2015 todate: 31-12-2015"}}

    This is the input: {user_prompt}
    '''

    try:
        # Make the API call to Gemini
        response = llm.invoke(prompt)
        
        # Extract the classification result
        classification_result = response.content.strip()
        
        # Try to parse as JSON, fallback if needed
        try:
            result_json = json.loads(classification_result)
            return json.dumps(result_json)
        except json.JSONDecodeError:
            # If not valid JSON, try to extract the search query
            if "search_query" in classification_result:
                return classification_result
            else:
                # Fallback: return the user prompt as search query
                return json.dumps({"search_query": user_prompt})
                
    except Exception as e:
        print(f"Error extracting search terms: {e}")
        # Fallback: return the user prompt as search query
        return json.dumps({"search_query": user_prompt})

# Main function for testing
if __name__ == "__main__":
    user_prompt = "Tell me about AstraZenca vs Intas Pharmaceuticals Limited case, what can you tell me about your mom"
    result = extract_search_terms(user_prompt)
    print("Search Query:", result)