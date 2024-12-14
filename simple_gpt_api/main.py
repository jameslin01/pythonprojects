# import library from PyPi
import openai

# set up api secret key from open ai

openai.api_key = 'your_open_ai_key'

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
        