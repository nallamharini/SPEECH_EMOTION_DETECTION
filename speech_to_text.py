import speech_recognition as sr

def speech_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Transcribed text: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
            return None

if __name__ == "__main__":
    audio_path = r"C:\Users\nalla\Desktop\SPEECH_EMOTION_DETECTION\DATASET\Actor_02"
    print(f"Result: {text}")

