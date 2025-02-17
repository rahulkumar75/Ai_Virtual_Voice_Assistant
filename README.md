# AI Virtual Voice Assistant
# Table of Contents
1. Introduction
2. High-level overview
3. Key Features
4. Technology Used
5. Installation
6. Usage
7. Code Overview
8. Main Script
9. Model Training
10. Intents JSON Structure
11. Task Modules
12. Future Enhancements
13. Contributors

# Introduction
Developed an AI-driven virtual voice assistant capable of understanding and responding to user commands through Natural Language Processing(NLP), Machine Learning,  and Neural Networks involving several components and techniques from these fields. This project integrated speech recognition, natural language understanding, and text-to-speech technologies to create a seamless, interactive user experience. The assistant was designed to perform the user's day-to-day various tasks, such as answering questions, making recommendations, controlling smart devices, showing weather reports, managing schedules, setting reminders, searching the web, creating reminders, setting Alarms, and providing personalized responses based on user preferences.

# High-level overview of the process and technologies involved:
- Data Collection: Text Data, Labeling
- Natural Language Processing (NLP): Tokenization, Part-of-Speech Tagging, Named Entity Recognition (NER), Dependency Parsing, Sentiment Analysis
- Model Selection: Intent Classification, Entity Recognition, Response Generation
- Model Training: Prepare Data, Train Models, Evaluate Models
- Integration: External APIs
- User Interface: Virtual Assistant Interface

# Key Features
* Speech Recognition: Implemented using Python's SpeechRecognition library, allowing the assistant to accurately convert spoken words into text.
* Natural Language Processing (NLP): Utilized Google's Dialogflow (or an equivalent NLP framework) to interpret user intents and extract meaningful information from the commands. This enabled the assistant to understand the context and provide relevant responses.
* Text-to-Speech (TTS): Integrated with a TTS engine (like Google Text-to-Speech or pyttsx3) to convert text responses into spoken words, creating an interactive, human-like interaction.
* Task Management: The assistant could manage tasks such as setting alarms, reminders, and calendar events, improving user productivity.
* Web Search and Information Retrieval: Integrated with web APIs to fetch information from the internet, such as weather updates, news, and general queries.
* Smart Device Control: Provided voice-activated control for IoT devices, allowing users to manage smart home appliances like lights, thermostats, and security systems.
* Customizable Responses: Included features for learning user preferences over time, allowing the assistant to deliver personalized responses and suggestions.
* Searching on Wikipedia, Google, and YouTube Managing alarms and schedules
* Controlling system functions (shutdown, volume control, etc.)
* Sending emails and taking screenshots
* User Authentication: Ensures security by verifying passwords.

# Technologies Used:
* Programming Languages: Python
* Libraries & Frameworks: SpeechRecognition, Google Text-to-Speech (TTS), Dialogflow, pyttsx3
* APIs: Google Cloud API, OpenWeatherMap API
* Tools: Git, Virtualenv
* Development Environment: Visual Studio Code

# Challenges Overcome:
* Noise Reduction in Speech Recognition: Implemented noise-cancelling techniques and fine-tuned the speech recognition parameters to improve accuracy in diverse environments.
* Contextual Understanding: Enhanced the assistant’s ability to maintain context across multiple interactions, improving the quality of conversations and user satisfaction.
* Real-Time Processing: Optimized the code for real-time processing to ensure that the assistant could respond promptly to user commands without noticeable lag.



# Installation
* Prerequisites
  - Python 3.12
  - PyTorch
  - NLTK
  - Other Python libraries as listed in requirements.txt
* Steps
1. Clone the Repository
git clone [https://github.com/rahulkumar75/Ai_Virtual_Voice_Assistant.git]
  - cd ai-virtual-assistant
    
2. Install Dependencies
  - pip install -r requirements.txt
3. Download NLTK Data
  - import nltk
  - nltk.download('Punkt)

4. Prepare Training Data
* Ensure intents.json is correctly formatted and located in the project directory.
* Train your model if not already trained. The training script should be included in your repository.
  
5. Run the Application
* python AI_ASSISTANT.py

# Usage
1. Start the Application
* Run the main script to start the virtual assistant.
* Ensure your microphone is working properly as the assistant listens to voice commands.
  
2. Interact with the Assistant

* Give voice commands such as "What is the time?" or "Search Wikipedia for Python programming".
* The assistant will process the command and provide a response or perform the requested action.
  
# Code Overview
* Main Script
* Imports and Configuration
  -Imports necessary libraries and configures the device for PyTorch.
  - Loads the intent file and trained model parameters.

* Main Function
  - Listens for user input.
  - Tokenizes and processes the input using the neural network model.
  - Matches the user input with predefined intents and executes the corresponding task.

* Model Training
  - Neural Network: The NeuralNet class defines the architecture of the neural network.
  - Training Script: The script for training the model on the intents.json data should be provided. This includes tokenizing the data, creating the bag of words, and training the model using PyTorch.
    
# Intents JSON Structure
The intents.json file contains various user intents and corresponding responses. Here is an example structure:
- {
-  "intents": [
-    {
-      "tag": "greeting",
-      "patterns": ["Hi", "Hello", "How are you?"],
-      "responses": ["Hello!", "Hi there!", "Greetings!"]
-    },
-    {
-      "tag": "time",
-     "patterns": ["What time is it?", "Tell me the time"],
-      "responses": ["The current time is..."]
-    }
-  ]
- }

# Task Modules
- Listen Module: Handles capturing audio input from the user.
- Speak Module: Manages converting text responses to speech.
- Task Module: Defines specific tasks that can be executed without or with additional input.

# Project Impact: 
This project provided a comprehensive hands-on experience in integrating AI with everyday tasks, showcasing the potential of virtual assistants in enhancing productivity and user experience. The successful deployment of this assistant demonstrated a strong grasp of AI concepts, Python programming, and API integration, reflecting a commitment to creating practical, user-friendly applications.

# Future Enhancements
* User Authentication: Enhance security features such as multi-factor authentication.
* Expanded Intents: Add more intents and corresponding tasks.
* Improved NLP: Integrate more advanced NLP techniques for a better understanding of user commands.
* GUI Interface: Develop a graphical user interface for ease of use.

