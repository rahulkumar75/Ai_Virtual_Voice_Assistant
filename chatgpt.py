# Importing necessary libraries
import openai
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
API = os.getenv("OPENAI_API_KEY")


def reply_brain(question, chat_log=None):
    chat_log_file = "chat_log.txt"  # Specify the file for chat log

    # Load chat log template from file
    if chat_log is None:
        with open(chat_log_file, "r") as file:
            chat_log = file.read()

    # Create the prompt for the AI assistant
    prompt = f"{chat_log}You: {question}\nAssistant: "

    # Request completion from OpenAI
    response = openai.Completion.create(
        model="gpt-3.5-turbo"
              "",  # Use 'text-davinci-003' or 'gpt-3.5-turbo'
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
    )

    # Extract the assistant's response
    answer = response.choices[0].text.strip()

    # Update the chat log
    chat_log += f"\nYou: {question}\nAssistant: {answer}"
    with open(chat_log_file, "w") as file:
        file.write(chat_log)

    return answer

# Test the function
reply = reply_brain("hello, how are you?")
print(reply)

