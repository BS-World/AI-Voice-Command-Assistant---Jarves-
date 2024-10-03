

---

# AI Voice Command Assistant - Jarves

This repository contains **Jarves**, an AI-based voice command assistant created by Bhanu Pratap Biswas. Jarves can listen to user commands, respond using text-to-speech, and perform tasks like opening and closing applications on your computer.

## Features

- **Voice Recognition**: Jarves uses the Google Speech Recognition API to convert speech into text.
- **Text-to-Speech**: It utilizes the `pyttsx3` library to speak responses back to the user.
- **App Control**: Jarves can open and close applications based on voice commands.
- **Cross-Platform Compatibility**: Works on both Windows and Linux systems.

## Requirements

To run this project, ensure you have the following libraries installed:

```bash
pip install SpeechRecognition
pip install pyttsx3
```

Additionally, you may need to install the following dependencies:

- For **Windows**:
  - Ensure that Python and pip are installed.
  - Make sure your microphone is working correctly.

- For **Linux**:
  - Install `espeak`, `pyaudio`, and `python3-dev` for full functionality.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/BS-World/AI-Voice-Command-Assistant---Jarves-.git
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Python script:
   ```bash
   python jarves.py
   ```

4. Say commands like:
   - "Hi Jarves" - To greet the assistant.
   - "Open [app name]" - To open an application.
   - "Close [app name]" - To close an application.
   - "Exit" or "Quit" - To exit the assistant.

## Example Commands

- "Hi Jarves" – Jarves will greet you.
- "Open notepad" – Opens the Notepad application (on Windows).
- "Close notepad" – Closes the Notepad application (on Windows).
- "Exit" – Terminates the program.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

---
