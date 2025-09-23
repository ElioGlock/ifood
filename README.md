# Voice-Controlled iFood Bot

This project is a Python-based application that combines a voice assistant ("Alicia") with a web automation bot ("Ielio") to log into the iFood website by voice command.

The user can activate the assistant with a hotkey, speak a command to place a predefined order, and the bot will automatically open a browser, navigate to iFood, and handle the entire login process, including the retrieval of the two-factor authentication code from an email account.

## Features

  * **Voice Activation**: The main script listens for a hotkey (F10) to activate the voice assistant.
  * **Speech Recognition**: Uses the `speech_recognition` library to process voice commands in Portuguese.
  * **Audio Feedback**: The assistant, "Alicia," provides spoken responses using Google Text-to-Speech (`gTTS`).
  * **Automated Browser Login**: The "Ielio" class uses `Selenium` to automate the login sequence on the iFood website.
  * **Automatic 2FA Code Retrieval**: The bot automatically connects to a specified Gmail account via IMAP to read the login code sent by iFood, enabling a hands-free login.
  * **Multi-threading**: The application runs the browser automation and the voice assistant in separate threads to ensure a responsive user experience.

## How It Works

1.  **Initialization**: The `main_file.py` script is the entry point. It waits for the user to press the **F10** key.
2.  **Activation**: Once F10 is pressed, an instance of the `Alicia` (voice assistant) and `Ielio` (iFood bot) classes are created.
3.  **Voice Command**: `Alicia` starts listening for a voice command through the microphone. It recognizes keywords for placing an order (like `"pedido"`, `"rápido"`) or quitting the application (`"sai"`, `"encerra"`).
4.  **Order Selection**: If an order command is given, Alicia will ask for which of the predefined orders to select (e.g., "one", "two", or "three") and confirm the choice with audio feedback.
5.  **Browser Automation**: Simultaneously, the `Ielio` class launches a Selenium-controlled Chrome browser and navigates to the iFood website.
6.  **Email and Code Verification**: The bot enters the email address and then connects to the Gmail account using `imbox` to find the most recent login email from iFood. It parses the 6-digit code from the email's subject line and types it into the verification fields on the website to complete the login.

## File Descriptions

  * **`main_file.py`**: The main executable script. It handles program initialization, hotkey listening, and orchestrates the `Alicia` and `Ielio` objects.
  * **`alicia_class.py`**: Defines the `Alicia` class, which manages all voice interactions, including speech-to-text and text-to-speech functionalities.
  * **`ifood_class.py`**: Defines the `Ielio` class, responsible for all web automation tasks using Selenium, including the process of logging into iFood and retrieving the access code from a Gmail inbox.

## Setup and Installation

### Prerequisites

  * Python 3.x
  * Google Chrome browser

### Dependencies

Install the required Python libraries using pip:

```bash
pip install speech_recognition gtts playsound selenium webdriver-manager imbox python-keyboard
```

### Configuration

1.  **Email Password**: Create a folder named `passwords` in the root directory. Inside it, create a file named `password_gmail` and place the password for your Gmail account in it. The `ifood_class.py` script reads from this file to log in to the email server.

2.  **Gmail Account Settings**: For the `imbox` library to access your emails, you must enable **"Less secure app access"** in your Google Account settings.

      * *Note: This makes your account more vulnerable. It is highly recommended to use an app-specific password or a dedicated email account for this project.*

## How to Run

1.  Ensure all dependencies are installed and the configuration is complete.
2.  Run the main script from your terminal:
    ```bash
    python main_file.py
    ```
3.  Press the **F10** key to activate the voice assistant.
4.  Speak your command when prompted by the audio cue. For example:
      * "Alicia, fazer o pedido de sempre."
      * The assistant will reply: "Qual pedido de sempre?"
      * "O pedido um."
5.  To terminate the program at any time, say a quit command like `"encerrar"`.
