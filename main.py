from ankify import *
import os
import subprocess
import shutil
from time import sleep
import mp3Processor

REDOWNLOAD_CORE = False

def clear_data():
    # Delete Core Data if REDOWNLOAD_CORE is True except for placeholder
    if REDOWNLOAD_CORE:
        for file in os.listdir("data/core"):
            if file != ".placeholder":
                os.remove(f"data/core/{file}")
        
    # Delete all files in clips folder except for placeholder
    for file in os.listdir("data/clips"):
        if file != ".placeholder":
            os.remove(f"data/clips/{file}")
    
    # Delete all other files in data folder.
    for file in os.listdir("data"):
        if file != "core" and file != "clips":
            os.remove(f"data/{file}")

def run():

    clear_data() # Empty data folder of all files besides placeholder
    
    mp3Processor.download("https://www.youtube.com/watch?v=r6cIKA1SWI8")

    # Remove vocals from audio and generate audio_Vocals.wav and audio_Instruments.wav
    mp3Processor.isolate_vocals()

    mp3Processor.clip_timestamp(0, 5, "mata0")

    deck = gen_deck("Anki Deck")
    model = gen_model("Anki Model")

    # The fields of the model specified in model_setup() detail how the note (flashcard) will be formatted
    note = genanki.Note(
        model, ["また月が昇る", "The moon is rising again", "[sound:mata0_src.mp3]", "[sound:mata0_vocals.mp3]"])
    deck.add_note(note)

    # Generate package
    pkg = genanki.Package(deck, ["data/clips/mata0_src.mp3", "data/clips/mata0_vocals.mp3"])
    pkg.write_to_file("data/anki_deck.apkg")


if __name__ == '__main__':
    run()
