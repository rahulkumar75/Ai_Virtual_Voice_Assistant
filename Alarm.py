import os
import time as time_module
import datetime
from Speak import Say
from Listen import Listen


# Function to handle alarm setup and ringing
def set_alarm():
    # Handle setting an alarm based on voice query
    # if "set an alarm" in query.lower():

        Say("Please specify the time for the alarm (e.g., '10:30').")
        # alarm_time = Listen().strip()
        alarm_time = input("Enter Time:")

        # Write the alarm time to the file
        with open("Alarmtext.txt", "w") as alarm_file:
            alarm_file.write(alarm_time)

        Say(f"Alarm set for {alarm_time}.")


# Function to ring the alarm at the specified time
def ring_alarm():
    # Read the alarm time from the file
    with open("Alarmtext.txt", "r") as alarm_file:
        alarm_time = alarm_file.read().strip()

    Say(f"Waiting for alarm at {alarm_time}.")

    # Infinite loop to check the time and ring the alarm if it matches
    while True:
        # Get the current time
        current_time = datetime.datetime.now().strftime("%H:%M")

        # Check if the current time matches the alarm time
        if current_time == alarm_time:
            Say("Alarm ringing, sir.")
            os.startfile("AlarmNotification.mp3")  # Play alarm sound
            # Clear the alarm time in the file
            with open("Alarmtext.txt", "w") as alarm_file:
                alarm_file.write("")
            break  # Exit the loop after ringing the alarm

        # Sleep for a short duration to avoid busy-waiting
        time_module.sleep(1)


# Main function to handle queries and set the alarm
def handle_alarm():
    set_alarm()
    ring_alarm()



# handle_alarm()

