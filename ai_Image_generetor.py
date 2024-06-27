import requests
import credential
from Speak import Say
from Listen import Listen


def generator_image():

    api_key = credential.image_api_key
    Say("Please Specify What Type Of Photos You Would Like To Receive.")
    userCommand = input("Enter Image Type: ")

    Say("Please say (yes) to confirm your command otherwise no!")


    # Get the user's response
    option = Listen()

    # Check if option is valid
    if option is None:
        # If Listen() returns None, prompt the user to try again
        Say("Sorry, I didn't catch that. Please speak YES or NO.")
        option = Listen()

    # Normalize the user's response to lowercase
    option = option.lower() if option else ""

    if "yes" in option:
        response = requests.post(
            f"https://api.stability.ai/v2beta/stable-image/generate/core",
            headers={
                "authorization": f"Bearer sk-{api_key}",
                "accept": "image/*"
            },
            files={"none": ''},
            data={
                "prompt": userCommand,
                "output_format": "png",
            },
        )

        if response.status_code == 200:
            with open("Ai_image_sample.png", 'wb') as file:
                file.write(response.content)
        else:
            raise Exception(str(response.json()))

    else:
        Say("Ok")
        



# generator_image()
