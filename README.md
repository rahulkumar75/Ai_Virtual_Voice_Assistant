# AI Virtual Assistant Documentation
# Table of Contents
1. Introduction
2. Features
3. Technology Stack
4. Installation
5. Usage
6. Code Overview
7. Main Script
8. Model Training
9. Intents JSON Structure
10. Task Modules
11. Future Enhancements
12. Contributors

# Introduction
This AI Virtual Assistant project leverages natural language processing (NLP) and deep learning to understand and respond to user commands. It is designed to perform a variety of tasks, from simple queries like time and date to more complex operations such as searching the internet and sending emails.

# Features
* Natural Language Understanding: Uses a neural network model to understand user commands.
* Task Execution: Performs a wide range of tasks including: Telling time, date, and day
* Searching on Wikipedia, Google, and YouTube Managing alarms and schedules
* Controlling system functions (shutdown, volume control, etc.)
* Sending emails and taking screenshots
* User Authentication: Ensures security by verifying passwords.

# Technology Stack
* Programming Language: Python
* Frameworks: PyTorch (for neural networks)
* NLP Libraries: NLTK (for tokenization and bag of words)
* Other Dependencies: random, json, torch
  
# Installation
* Prerequisites
  - Python 3.12
  - PyTorch
  - NLTK
  - Other Python libraries as listed in requirements.txt
* Steps
1. Clone the Repository
git clone https://github.com/yourusername/ai-virtual-assistant.git
  - cd ai-virtual-assistant
    
2. Install Dependencies
  - pip install -r requirements.txt
3. Download NLTK Data
  - import nltk
  - nltk.download('punkt')

4. Prepare Training Data
* Ensure intents.json is correctly formatted and located in the project directory.
* Train your model if not already trained. The training script should be included in your repository.
  
5. Run the Application
* python AI_ASSISTANT.py

# Usage
1. Start the Application
* Run the main script to start the virtual assistant.
* Ensure your microphone is working properly as the assistant listens for voice commands.
  
2. Interact with the Assistant

* Give voice commands such as "What is the time?" or "Search Wikipedia for Python programming".
* The assistant will process the command and provide a response or perform the requested action.
  
# Code Overview
* Main Script
* Imports and Configuration
  -Imports necessary libraries and configures the device for PyTorch.
  - Loads the intents file and trained model parameters.

* Main Function
  - Listens for user input.
  - Tokenizes and processes the input using the neural network model.
  - Matches the user input with predefined intents and executes the corresponding task.

* Model Training
  - Neural Network: The NeuralNet class defines the architecture of the neural network.
  - Training Script: The script for training the model on the intents.json data should be provided. This includes tokenizing the data, creating the bag of words, and training the model using PyTorch.
    
# Intents JSON Structure
The intents.json file contains various user intents and corresponding responses. Here is an example structure:
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "How are you?"],
      "responses": ["Hello!", "Hi there!", "Greetings!"]
    },
    {
      "tag": "time",
      "patterns": ["What time is it?", "Tell me the time"],
      "responses": ["The current time is..."]
    }
  ]
}

# Task Modules
- Listen Module: Handles capturing audio input from the user.
- Speak Module: Manages converting text responses to speech.
- Task Module: Defines specific tasks that can be executed without or with additional input.

# Future Enhancements
* User Authentication: Enhance security features such as multi-factor authentication.
* Expanded Intents: Add more intents and corresponding tasks.
* Improved NLP: Integrate more advanced NLP techniques for a better understanding of user commands.
* GUI Interface: Develop a graphical user interface for ease of use.
# Contributors
* Name: @Rahul @Amisha @Anisha
Feel free to reach out to me at rahulkumarx333@gmail.com for any questions or contributions.
