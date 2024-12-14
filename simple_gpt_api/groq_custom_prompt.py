# import library from PyPi
import os
from dotenv import load_dotenv # helps to obtain API key from .env file
from groq import Groq

load_dotenv()

# set up Groq client

client = Groq(api_key = os.environ.get("GROQ_API_KEY"))


# Set the system prompt to decide on the vibe of the chatbot

choose_prompt = input("Choose the vibe for your bot")

system_prompt = {
    "role": "system",
    "content":
    choose_prompt
}

# set up the exit prompt to display the vibe of chatbot when you stop using it

exit_prompt = {
    "role": "system",
    "content":
    "You are about to be left. You reply with a message indicating that you are sad that the user is going to stop using you"
}

# intialise chat history without the chatbot replying

chat_history = [system_prompt]

while True:
    # Get user input from the console
    user_input = input("You: ")
    
    # Append the user input to the chat history
    chat_history.append({"role": "user",
                          "content": user_input})
    
    if user_input.lower() in ["quit", "stop", "bye"]:

        chat_history = [exit_prompt]
        # use the openai api
        response = client.chat.completions.create(model = "llama3-70b-8192",
                                                  
                                                  messages = chat_history,
                                                  
                                                  temperature = 1.2)
        
        # print the sad response

        print("Assistant:",
              response.choices[0].message.content)
        break    

    response = client.chat.completions.create(model = "llama3-70b-8192",
                                              # a list of message parameters where each message is used to construct the dialogue or prompt for the model
                                              messages = chat_history,
                                              # maxinum number of tokens to generate in the completion
                                              max_tokens = 100,
                                              # controls randomness in output generation
                                              temperature = 1.2
    )
    
    # Append the response to the chat history                                          
    chat_history.append({
        "role": "assistant",
        "content": response.choices[0].message.content

    })

    # print the response
    print("Assistant:",
          response.choices[0].message.content)
    