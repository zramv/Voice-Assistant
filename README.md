# Voice Assistant
An intelligent voice assistant that listens to your spoken questions, sends them to an AI model (Cohere), and replies with a spoken answer using text-to-speech.

## How It Works

This voice assistant follows a simple 4-step process using Python libraries and Cohere AI:

1. **Voice Input (`speech_recognition`)**  
   The assistant listens through the microphone and captures the user's spoken question using the speech_recognition library.

2. **Speech-to-Text**  
   The recorded audio is transcribed into plain text using Google's Web Speech API (via `speech_recognition`).

3. **AI Response (`Cohere`)**
   The text is sent to Cohere’s language model, which generates a smart, natural-language answer based on the user's input.

4. **Text-to-Speech (`gTTS`)**
   The AI-generated response is converted back to speech using the gTTS (Google Text-to-Speech) library and played aloud.

5. **Continuous Loop** 
   After speaking the response, the assistant automatically returns to listening for the next question.


## Technologies Used
This project build using the following tools and libraries::
- **Python**
- **speech_recognition**
- **Cohere**
- **gTTS**
- **pygame / tempfile**

## Example

https://github.com/user-attachments/assets/6d8454e0-3fb4-49c5-adf4-de819c3649f5

