# import library from PyPi
import os
from dotenv import load_dotenv # helps to obtain API key from .env file
import openai

# set up api secret key from open ai

openai.api_key = os.environ.get("API_KEY")

def chat_with_gpt(prompt):
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role": "user",
                "content": prompt
            }
                      
                      ]
    )
    
    return response.choices[0].messages.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You:")
        if user_input.lower() in ["quit",
                                   "exit",
                                   "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
        