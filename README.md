# Voice Chat Application

This project is a simple real-time voice chat application built using Python. It allows users to communicate over a network using voice data, leveraging socket programming and audio processing capabilities.

## Features
- Real-time voice communication between a server and a client.
- Uses Python's `socket` module for network communication.
- Employs the `pyaudio` library for audio input/output.
- Scalable design capable of handling multiple clients.

## Requirements
- Python 3.x
- Libraries: `pyaudio`, `socket`
- Microphone and speakers for audio input/output

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
2. Install the required libraries:
   ```bash
   pip install pyaudio

## Usage

### Server
1. Navigate to the server directory:
   ```bash
   python cn-project-server.py
2. The server will start listening for incoming connections.

### Client
1. Update the host_ip in cn-project-client.py to match the server's IP address.
2. Run the client script:
   ```bash
   python cn-project-client.py
3. Begin speaking into the microphone to transmit audio to the server.

## Project Structure
- **cn-project-server.py**: Contains the server-side implementation for receiving and playing audio data.
- **cn-project-client.py**: Contains the client-side implementation for capturing and sending audio data.
- **Documentation**: Includes the project report and detailed explanations.

## How it Works
1. The server listens for incoming connections on a specified port.
2. Once a client connects, audio data is captured using the `pyaudio` library and transmitted using sockets.
3. The server receives the data and plays it back in real time.

