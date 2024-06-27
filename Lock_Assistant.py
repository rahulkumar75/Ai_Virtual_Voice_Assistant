import sys
from Speak import Say
from Listen import Listen
from colorama import init, Fore, Back, Style    # pip install colorama

# Initialize colorama
init()
from getpass import getpass

# Define the maximum number of password attempts
MAX_ATTEMPTS = 3


def verify_password():
    """
    Verify the user's password to access the assistant.
    """
    Say("Verification Start..")
    Say("Please Tell Me The Password To Authenticate Yourself!")
    for attempt in range(MAX_ATTEMPTS):
        # Use a secure method to hide password input
        # password_attempt = getpass("Enter password to open Jarvis: ")
        # password_attempt = Listen().strip()  # Use voice input for password
        password_attempt = input("Enter Password: ")

        # Read the stored password from the file
        with open("password.txt", "r") as pw_file:
            stored_password = pw_file.read().strip()

        # Compare the input password with the stored password
        if password_attempt == stored_password:
            Say("Verification Process Successfully Completed")
            Say("Welcome,sir! I Am Ready To Assist You!")
            from GreetMe import greetMe
            greetMe()
            return True
        else:
            Say("Incorrect password, try again.")


    # If the user fails all attempts, exit the program
    Say("Maximum password attempts reached. Exiting.")
    exit()


def change_password(query):
    """
    Change the user's password.
    """
    if "change password" in query.lower():
        Say("What is the new password?")

        # Use a secure method to hide password input
        # new_password = getpass("Enter the new password: ")
        new_password = input("Enter the new password: ")

        # Write the new password to the file
        with open("password.txt", "w") as pw_file:
            pw_file.write(new_password)

        Say("Your new password has been set successfully.")
        Say(f"Your new password is: {new_password}")


# Example usage:
# query = Listen()

# if verify_password():
#     # AI assistant functionality
#     # pass
#     query = Listen()
#     change_password("change password")


