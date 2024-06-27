from Speak import Say


def change_password():
    """
    Change the user's password.
    """
    Say("What is the new password?")

    # Use a secure method to hide password input
    # new_password = getpass("Enter the new password: ")

    new_password = input("Enter the new password: ")

    # Write the new password to the file
    with open("password.txt", "w") as pw_file:
        pw_file.write(new_password)

    Say("Your new password has been set successfully.")
    # Say(f"Your new password is: {new_password}")