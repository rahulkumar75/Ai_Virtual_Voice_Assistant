from Lock_Assistant import verify_password
import random
import json
import torch.cuda
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open("intents.json", "r") as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# -----------------------------------------------------

Name = "AI Virtual Assistant"
from Listen import Listen
from Speak import Say
from Task import NonInputExecution
from Task import InputExecution


def Main():
        sentence = Listen()
        query = str(sentence)

        if sentence == "bye":
            Say("Going to sleep,Thank You")
            exit()

        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)

        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.75:
            for intent in intents["intents"]:
                if tag == intent["tag"]:
                    reply = random.choice(intent["responses"])
                    # reply => RandomResponse by Model, query => str(sentence) == Command by user

                    # Task Implementation----
                    if "time" in reply:
                        NonInputExecution(reply)

                    elif "date" in reply:
                        NonInputExecution(reply)

                    elif "day" in reply:
                        NonInputExecution(reply)

                    elif "wikipedia" in reply:
                        InputExecution(reply, sentence)

                    elif "alarm" in reply:
                        InputExecution(reply, query)

                    elif "random advice" in reply:
                        NonInputExecution(reply)

                    elif "translate" in reply:
                        InputExecution(reply, query)

                    elif "internet speed" in reply:
                        NonInputExecution(reply)

                    elif "movie" in reply:
                        InputExecution(reply, tag)

                    elif "news" in reply:
                        InputExecution(reply, query)

                    elif "temperature" in reply:
                        InputExecution(reply, query)

                    elif "open" in reply:
                        InputExecution(reply, query)

                    elif "close" in reply:
                        InputExecution(reply, query)

                    elif "search on google" in reply:
                        InputExecution(reply, query)

                    elif "search on youtube" in reply:
                        InputExecution(reply, query)

                    elif "whatsapp" in reply:
                        InputExecution(reply, query)

                    elif "change password" in reply:
                        InputExecution(reply,query)

                    elif "screenshot" in reply:
                        NonInputExecution(reply)

                    elif "take my photo" in reply:
                        NonInputExecution(reply)

                    elif "ai image" in reply:
                        InputExecution(reply,query)

                    elif "game" in reply:
                        NonInputExecution(reply)

                    elif "ip address" in reply:
                        NonInputExecution(reply)

                    elif "schedule my day" in reply:
                        InputExecution(reply,query)

                    elif "show my schedule" in reply:
                        InputExecution(reply,query)

                    elif "shutdown system" in reply:
                        NonInputExecution(reply)

                    elif "play" in reply:
                        NonInputExecution(reply)

                    elif "pause" in reply:
                        NonInputExecution(reply)

                    elif "mute" in reply:
                        NonInputExecution(reply)

                    elif "unmute" in reply:
                        NonInputExecution(reply)

                    elif "volume up" in reply:
                        NonInputExecution(reply)

                    elif "volume down" in reply:
                        NonInputExecution(reply)

                    elif "remember that" in reply:
                        NonInputExecution(reply)

                    elif "do you remember anything" in reply:
                        NonInputExecution(reply)

                    elif "send email" in reply:
                        InputExecution(reply,query)


                    else:
                        Say(reply)

if verify_password():
    while True:
        Main()
