from Speak import Say
import smtplib
import getpass




def send_mail():
    """Send an email."""
    Say("Please enter the sender's email address.")
    email = input("SENDER EMAIL: ")

    Say("Please enter the receiver's email address.")
    receiver_email = input("RECEIVER EMAIL: ")

    Say("Please enter the subject of your email.")
    subject = input("SUBJECT: ")

    Say("Please enter your message.")
    message = input("MESSAGE: ")

    text = f"Subject: {subject}\n\n{message}"

    try:
        # Set up the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        Say("Please enter your email password:")
        # password = getpass.getpass("PASSWORD: ")
        password = input("PASSWORD: ")

        server.login(email, password)

        server.sendmail(email, receiver_email, text)
        Say("Your email has been sent successfully.")
        print(f"Email has been sent to: {receiver_email}")
    except Exception as e:
        Say("There was an error sending the email. Please try again.")
        print(f"Error: {e}")
    finally:
        server.quit()

# Call the function to send an email
# send_mail()
