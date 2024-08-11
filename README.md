# Navttc-Task-13-Text-to-speech-

# Text-to-Speech Converter

## Description

This Python script converts text to speech using the `pyttsx3` library. It offers two modes: converting text from user input or from a text file.

## Code

```python
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
```

## Steps

1. **Import Required Module:**
   - Import the `pyttsx3` library, which is used to convert text to speech.

2. **Define the `text_to_speech` Function:**
   - This function initializes the text-to-speech engine and converts the provided text into speech.

3. **Define the `text_to_speech_from_file` Function:**
   - This function reads text from a specified file and converts it to speech using the `text_to_speech` function.
   - It handles exceptions, such as file not found errors.

4. **Main Program:**
   - The user is prompted to choose between entering text manually or providing a file path to read the text from.
   - Depending on the user's choice, the script will either convert the entered text or the text from the file to speech.

## How to Run

1. **Ensure Python and Required Libraries are Installed:**
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
   - Install the required `pyttsx3` library using the following command:
     ```bash
     pip install pyttsx3
     ```

2. **Save the Script:**
   - Save the provided Python code into a file named `13-Text to speech (Nasir Sharif).py`.

3. **Execute the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `13-Text to speech (Nasir Sharif).py` is saved.
   - Run the script using the following command:
     ```bash
     python 13-Text to speech (Nasir Sharif).py
     ```

4. **Enter Text or File Path:**
   - Choose whether to input text directly or provide a file path, then follow the prompts to convert the text to speech.

## Example

- **Option 1:** If you choose to enter text manually, you might input `"Hello World!"`, and the script will speak out the phrase.
- **Option 2:** If you choose to convert text from a file, provide the path to a `.txt` file, and the script will read and speak the text content.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact Nasir Sharif at nasirsharifqasoori786@gmail.com
