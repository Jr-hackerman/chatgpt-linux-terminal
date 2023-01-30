import requests
import json

def chat(query, api_key):
    # Make a request to the OpenAI API with the query and API key
    response = requests.post("https://api.openai.com/v1/engines/davinci/jobs", 
                             headers={"Content-Type": "application/json",
                                      "Authorization": f"Bearer {api_key}"},
                             data=json.dumps({"prompt": query,
                                              "max_tokens": 100,
                                              "temperature": 0.5}))
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract relevant information from the response
        response_json = response.json()
        return response_json["choices"][0]["text"]
    else:
        # Print an error message if the request was not successful
        print(f"Request failed with status code {response.status_code}")
        return None

# Example usage:
api_key = "<YOUR_API_KEY>"
while True:
    query = input("You: ")
    response = chat(query, api_key)
    if response is not None:
        print(f"ChatGPT: {response}")
    else:
        print("ChatGPT: I'm sorry, I couldn't understand your query. Please try again.")
