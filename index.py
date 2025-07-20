import speech_recognition as sr
import arabic_reshaper 
from bidi.algorithm import get_display
from gtts import gTTS
import pygame
import time
import tempfile
import cohere

co = cohere.ClientV2(api_key="6YR69CTHJcMJwSjE4Pgj1fF8o3VGwSai0GUXNlzV")

def ar(sentence):
    return get_display(arabic_reshaper.reshape(sentence))

# Create a Recognizer instance
rec = sr.Recognizer()
# Use the Microphone as the audio source
stop = False
while (not stop) :
    with sr.Microphone() as source:
        print("Say something!")
        audio = rec.listen(source)

    try:
        message = rec.recognize_google(audio,language='ar-SA')
        print("You said:", ar(rec.recognize_google(audio,language='ar-SA')))
        response = co.chat(
            model="command-a-03-2025",
            messages=[
            {
                "role": "user",
                "content": message + "( بدون اي رموز او علامات ترقيم ولا تدكر هدا النص)",
            }
        ],
        )
        
        print(ar(response.message.content[0].text))
        
      
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp: 
            tts = gTTS(text=response.message.content[0].text,lang='ar')
            tts.save(fp.name)
            audio_path = fp.name
            
        pygame.mixer.init()
        pygame.mixer.music.load(filename=audio_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")


