import ankify
import os
import mp3Processor
import srtProcessor

REDOWNLOAD_CORE = True

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

def run(link, name="Anki Deck"):

    clear_data() # Empty data folder of all files besides placeholder
    
    mp3Processor.download(link)

    # Remove vocals from source audio and generate audio_Vocals.wav and audio_Instruments.wav
    mp3Processor.isolate_vocals()

    deck = ankify.gen_deck(name)
    model = ankify.gen_model("My Model")

    # Parse SRT file
    note_field_lists, audio_paths = srtProcessor.processSrtFile("./lyrics.srt")
    
    # Add notes to deck
    ankify.add_notes(deck, model, note_field_lists)

    # Generate package
    ankify.gen_package(deck, audio_paths)


if __name__ == '__main__':
    run("https://www.youtube.com/watch?v=r6cIKA1SWI8", "Spinning Sky Rabbit")
