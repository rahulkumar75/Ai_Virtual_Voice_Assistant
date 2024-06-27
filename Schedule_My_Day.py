from Speak import Say
from Listen import Listen
from plyer import notification  # pip install plyer
from pygame import mixer  # pip install pygame

# Filepath for tasks
TASKS_FILE = "schedule_tasks.txt"


def clear_old_tasks():
    """
    Clear the existing tasks and prompt user for new tasks.
    """
    Say("Do you want to clear old tasks? Please speak YES or NO.")

    # Get the user's response
    option = Listen()

    # Check if option is valid
    if option is None:
        # If Listen() returns None, prompt the user to try again
        Say("Sorry, I didn't catch that. Please speak YES or NO.")


    # Normalize the user's response to lowercase
    option = option.lower() if option else ""

    if "yes" in option:
        with open(TASKS_FILE, "w") as file:
            file.write("")  # Clear the file
        Say("Old tasks cleared.")
        add_new_tasks()
    else:
        Say("Old tasks not cleared.")
        Say("Your Added Task is Here")
        file = open(TASKS_FILE, "r")
        content = file.read()
        file.close()
        mixer.init()
        mixer.music.load("ScheduleNotification.mp3")
        mixer.music.play()
        notification.notify(
            title="My schedule :-",
            message=content,
            timeout=15
        )


def add_new_tasks():
    """
    Prompt the user to add new tasks.
    """
    Say("How many tasks would you like to add?")
    try:
        # Get the number of tasks from voice input
        # num_tasks = int(Listen())
        num_tasks = int(input("Enter no. of Tasks"))

        tasks = []
        i = 0
        for i in range(num_tasks):
            Say(f"Please state task {i + 1}:")
            task = Listen()
            tasks.append(task)
            # Save each task to the tasks file
            with open(TASKS_FILE, "a") as file:
                file.write(f"{i + 1}. {task}\n")

        Say(f"Added {num_tasks} tasks to your schedule.")
    except ValueError:
        Say("Invalid number of tasks. Please try again.")


def show_schedule():
    """
    Read and display the user's schedule.
    """
    try:
        with open(TASKS_FILE, "r") as file:
            content = file.read()

        mixer.init()
        mixer.music.load("ScheduleNotification.mp3")
        mixer.music.play()

        # Display notification with the schedule
        notification.notify(
            title="My schedule :-",
            message=content,
            timeout=15
        )

        # Voice feedback for the schedule
        Say("Here is your schedule:")
        Say("\n" + content)
        Say("Thank You")
    except Exception as e:
        Say(f"An error occurred while showing your schedule: {e}")


