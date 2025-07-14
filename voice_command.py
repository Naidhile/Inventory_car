import speech_recognition as sr
from user_functions import get_top_trending_products

def voice_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening for command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Command received: {command}")
        return command
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return ""

def handle_voice_command(command):
    if "top trending products" in command:
        top_products = get_top_trending_products()
        for product in top_products:
            print(f"Product ID: {product[0]}, Sales Count: {product[1]}")
    # Add more voice commands as needed

# Example usage
if __name__ == "__main__":
    command = voice_command()
    handle_voice_command(command)
