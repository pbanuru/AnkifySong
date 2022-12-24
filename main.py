import ankify
import os
import sys
import mp3Processor
import srtProcessor

REDOWNLOAD_CORE = False
DEBUG = True

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

def run(link, name="Anki Deck", srt_path="./lyrics.srt"):

    clear_data() # Empty data folder of all files besides placeholder
    
    song = mp3Processor.Song(link)

    # Parse SRT file
    srt_processor = srtProcessor.SrtProcessor(song, srt_path, 0.5)
    note_field_lists, audio_paths = srt_processor.processSrtFile()

    deck = ankify.gen_deck(name)
    model = ankify.gen_model("My Model")

    # Add notes to deck
    ankify.add_notes(deck, model, note_field_lists)

    # Generate package
    ankify.gen_package(deck, audio_paths)


if __name__ == '__main__':
    if DEBUG:
        run("https://www.youtube.com/watch?v=r6cIKA1SWI8", "Spinning Sky Rabbit")
        exit(0)

    argc = len(sys.argv)

    if argc not in [3, 4]:
        print("Usage: python3 main.py \"<youtube-link>\" \"<deck-name>\" [<srt-path>]")
        print("Using Default lyrics.srt file:\npython3 main.py \"https://www.youtube.com/watch?v=r6cIKA1SWI8\" \"Spinning Sky Rabbit\"")
        print("To specify srt path:\npython3 main.py \"https://www.youtube.com/watch?v=r6cIKA1SWI8\" \"Spinning Sky Rabbit\" .../.../mylyrics.srt")
        exit(1)
    
    link = sys.argv[1]
    name = sys.argv[2]

    if argc == 3:
        run(link, name)
    else:
        srt_path = sys.argv[3]
        run(link, name, srt_path)
