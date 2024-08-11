import pyttsx3

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties before adding anything to say
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
    
    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

def text_to_speech_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text_to_speech(text)
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main Program
choice = input("Do you want to convert text (1) from user input or (2) from a text file? Enter 1 or 2: ")

if choice == '1':
    user_text = input("Enter the text you want to convert to speech: ")
    text_to_speech(user_text)
elif choice == '2':
    file_path = input("Enter the file path: ")
    text_to_speech_from_file(file_path)
else:
    print("Invalid choice. Please enter 1 or 2.")
