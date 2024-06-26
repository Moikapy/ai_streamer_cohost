# AI Co-Host Project

This project is designed to create an AI co-host that can interact in real-time, capturing screen content, reading text from images, and communicating via WebSocket. The AI co-host is built using Python, LangChain, and FastAPI, and it integrates with Twitch to read chat messages. It also includes conversation memory using SQLite to store and retrieve messages for each session.

## Features

- 2D Avatar (wip)
- Real-time screen capture (wip)
- Real-time microphone input (wip)
- Real-time Twitch chat reading (wip)
- Communication via WebSocket
- Conversation memory with SQLite

## Prerequisites

- Python 3.10+
- Tesseract OCR

## Installation

### Step 1: Clone the Repository

````bash
git clone https://github.com/Moikapy/ai_streamer_cohost.git
cd ai_streamer_cohost
````

## Step 2: Install Python Dependencies
Create a virtual environment and install the required packages:

  ```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
````

Step 3: Install Tesseract OCR

Windows
Download the Tesseract installer from Tesseract at UB Mannheim.
Run the installer and follow the on-screen instructions.
Add the Tesseract installation path (e.g., C:\Program Files\Tesseract-OCR) to your system's PATH environment variable.

macOS
Install Tesseract using Homebrew:

```bash
brew install tesseract
Linux
Install Tesseract using your package manager. For example, on Debian-based systems like Ubuntu:
```

```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
Step 4: Verify Tesseract Installation
Open a new command prompt or terminal window and run:
```

```bash
tesseract --version
You should see the version information of Tesseract if it is correctly installed and added to your PATH.

Step 5: Configure Environment Variables
Create a .env file in the root of the project and add your OpenAI API key:
```

```bash
OPENAI_API_KEY=your_openai_api_key
Step 6: Run the Project
To start both the FastAPI server and the WebSocket client and monitor them for specific log messages, run:
```

```bash
python monitor_and_restart.py
Project Structure
```

```bash
├── app
│   ├── __init__.py
│   ├── image_processor.py
│   ├── langchain_client.py
│   ├── screen_capture_tool.py
│   ├── server.py
├── websocket_client.py
├── run_servers.py
├── monitor_and_restart.py
├── requirements.txt
├── .env
└── README.md
```

## Files Description

- app/image_processor.py: Handles image processing and OCR using Tesseract.
- app/langchain_client.py: Integrates with LangChain to handle AI responses and streaming, with conversation memory using SQLite.
- app/screen_capture_tool.py: Captures screen content.
- app/server.py: FastAPI server to handle WebSocket connections.
- websocket_client.py: WebSocket client to communicate with the FastAPI server.
- run_servers.py: Script to start both the FastAPI server and WebSocket client concurrently.
- monitor_and_restart.py: Script to monitor the server log and restart the server and client if necessary.
- requirements.txt: List of Python dependencies.
- .env: Environment variables file to store sensitive data like API keys.
- README.md: This file.

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

```bash

### Additional Notes

- Make sure that Tesseract OCR is properly installed and configured on your system to avoid any issues with image processing.
- The `.env` file should be created in the root of your project directory with the correct API key.

This `README.md` provides comprehensive instructions to get your project started and should help new contributors understand how to set up and run the project.
```
