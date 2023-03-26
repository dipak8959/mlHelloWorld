from gtts import gTTS
import os

# define a dictionary of greetings in different languages
greetings = {
    "english": "Hello!",
    "spanish": "¡Hola!",
    "french": "Bonjour!",
    "german": "Hallo!",
    "italian": "Ciao!",
    "japanese": "こんにちは！",
    "chinese": "你好！",
    "arabic": "مرحبا!"
}

# get the path of the directory where the script is located
script_dir = os.getcwd()

# prompt the user to enter a language
lang = input("Enter a language (e.g. english, spanish, french): ")

# generate the greeting for the specified language
if lang.lower() in greetings:
    greeting = greetings[lang.lower()]

    # create a gTTS object with the greeting text and the language
    lang_code = lang.lower()
    if lang.lower() == "english":
        lang_code = "en-US"
    elif lang.lower() == "french":
        lang_code = "fr"
    tts = gTTS(text=greeting, lang=lang_code)

    # save the audio file to disk
    filename = f"greeting_{lang.lower()}.mp3"
    file_path = os.path.join(script_dir, filename)
    tts.save(file_path)

    # play the audio file
    os.system(f"start {filename}")
else:
    print("Invalid language specified.")
