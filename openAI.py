import openai

openai.api_key=""

# completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     message=[{
#         "role": "user",
#         "content": "what is ai"
#
#     }]
# )
# print(completion.choices[0].message.content)

def openAi():
    messages = []
    system_msg = input("What type of chatbot would you like to create?\n")
    messages.append({"role": "system", "content": system_msg})

    print("Your new assistant is ready!")
    while input != "quit()":
        message = input()
        messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        print("\n" + reply + "\n")

openAi()