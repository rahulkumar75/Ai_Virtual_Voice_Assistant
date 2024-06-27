from Speak import Say
from Listen import Listen
import random


def game_play():
    Say("LETS PLAY ROCK PAPER SCISSORS!")
    print("LETS PLAAAAYYYYYYYYYYYYYYYYYYYY!!")

    Say("Please tell me participant name")
    ME = Listen()
    ME = str(ME)

    i = 0
    Me_score = 0
    Com_score = 0

    while i < 5:
        choose = ("rock", "paper", "seizures")
        com_choose = random.choice(choose)
        query = Listen()
        if query == "rock":
            if com_choose == "rock":
                Say("ROCK")
                print(f"Score:- {ME} : {Me_score} : Computer : {Com_score}")
            elif com_choose == "paper":
                Say("paper")
                Com_score += 1
                print(f"Score:- {ME} : {Me_score} : Computer : {Com_score}")
            else:
                Say("Scissors")
                Me_score += 1
                print(f"Score: {ME} : {Me_score} : Computer : {Com_score}")

        elif query == "paper":
            if com_choose == "rock":
                Say("ROCK")
                Me_score += 1
                print(f"Score: {ME} : {Me_score} : Computer :{Com_score}")
            elif com_choose == "paper":
                Say("paper")
                print(f"Score: {ME} : {Me_score} :: Computer :{Com_score}")
            else:
                Say("seizures")
                Com_score += 1
                print(f"Score: {ME} : {Me_score} :: Computer :{Com_score}")

        elif query == "scissors" or query == "seizures" or query == "Caesar":
            if com_choose == "rock":
                Say("ROCK")
                Com_score += 1
                print(f"Score: {ME} : {Me_score} :: Computer : {Com_score}")
            elif com_choose == "paper":
                Say("paper")
                Me_score += 1
                print(f"Score: {ME} : {Me_score} :: Computer :{Com_score}")
            else:
                Say("Scissors")
                print(f"Score: {ME} : {Me_score} :: Computer : {Com_score}")
        i += 1

    print(f"FINAL SCORE : {ME} : {Me_score} :: Computer : {Com_score}")

    if Me_score > Com_score:
        Say(f"Winner : {ME}")
    else:
        Say("Winner : Computer")

