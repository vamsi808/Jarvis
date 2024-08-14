# Jarvis
A virtual assistant script in Python using libraries like pyttsx3 for text-to-speech, speech_recognition for speech-to-text, and PyPDF2 for reading PDFs. It can perform tasks such as opening applications, sending emails, fetching news, and interacting with web services like Wikipedia and social media platforms.

# Virtual Assistant in Python

This project is a Python-based virtual assistant capable of performing various tasks such as speech recognition, text-to-speech conversion, opening applications, fetching news, reading PDFs, sending emails, and interacting with web services like Wikipedia and social media platforms.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Text-to-Speech**: Uses `pyttsx3` to convert text to speech.
- **Speech Recognition**: Utilizes `speech_recognition` for recognizing spoken commands.
- **Application Control**: Can open various applications such as Excel, PowerPoint, and Command Prompt.
- **Web Interaction**: Capable of searching on Wikipedia, playing songs on YouTube, and sending messages on WhatsApp.
- **Email Functionality**: Sends emails via Gmail using the `smtplib` library.
- **News Updates**: Fetches the latest news headlines.
- **PDF Reading**: Reads text from PDF files.
- **System Control**: Commands to shut down, restart, or perform other system operations.
- **Social Media Interaction**: Opens profiles on Instagram and downloads profile pictures.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/virtual-assistant-python.git
    cd virtual-assistant-python
    ```

2. **Install the Required Packages**
    Ensure you have Python 3.6 or higher installed. Then, run:
    ```bash
    pip install -r requirements.txt
    ```

3. **Add Your API Keys**
    Some features like news updates require API keys. Insert your keys where needed in the script:
    - `News API`: Replace the placeholder with your API key in the `news()` function.

## Usage

1. **Running the Virtual Assistant**
    ```bash
    python code2.py
    ```
    The assistant will greet you and await your command.

2. **Available Commands**
    - **"Open Excel"**: Opens Microsoft Excel.
    - **"Tell me news"**: Fetches the latest news headlines.
    - **"Play music"**: Plays the specified song.
    - **"Send an email to [name]"**: Sends an email.
    - **"Read PDF"**: Reads out loud the text from a PDF file.
    - **"Search Wikipedia for [query]"**: Fetches summary from Wikipedia.
    - **"Open [website]"**: Opens the specified website.
    - **"Shutdown the system"**: Shuts down the computer.

3. **Voice Commands**
    Simply speak out the command after the prompt. The assistant will recognize and execute it.

## Dependencies

The project requires the following Python packages:

- `pyttsx3`
- `speech_recognition`
- `pyaudio`
- `wave`
- `requests`
- `wikipedia`
- `pyautogui`
- `pyjokes`
- `selenium`
- `webbrowser`
- `pywhatkit`
- `smtplib`
- `instaloader`
- `PyPDF2`

You can install all dependencies using:
```bash
pip install -r requirements.txt
