from ankifysong import ankify
from ankifysong import mp3Processor
from ankifysong import srtProcessor
import os
import sys
import argparse

REDOWNLOAD_CORE = False
DEBUG = True

def clear_data():
    # Delete Core Data if REDOWNLOAD_CORE is True except for placeholder
    if REDOWNLOAD_CORE:
        for file in os.listdir("ankifysong/data/core"):
            if file != ".placeholder":
                os.remove(f"ankifysong/data/core/{file}")
        
    # Delete all files in clips folder except for placeholder
    for file in os.listdir("ankifysong/data/clips"):
        if file != ".placeholder":
            os.remove(f"ankifysong/data/clips/{file}")
    
    # Delete all other files in data folder.
    for file in os.listdir("ankifysong/data"):
        if file != "core" and file != "clips":
            os.remove(f"ankifysong/data/{file}")

def run(link, name, srt_path="ankifysong/lyrics.srt", output_path="ankifysong/data/anki_deck.apkg"):

    clear_data() # Empty data folder of all files besides placeholder
    
    song = mp3Processor.Song(link)

    # Parse SRT file
    # Buffer set to 0.5 seconds by default, can be changed
    srt_processor = srtProcessor.SrtProcessor(song, srt_path, 0.5)
    note_field_lists, audio_paths = srt_processor.processSrtFile()

    deck = ankify.gen_deck(name)
    model = ankify.gen_model("My Model")

    # Add notes to deck
    ankify.add_notes(deck, model, note_field_lists)

    # Generate package
    ankify.gen_package(deck, audio_paths, output_path)

if __name__ == '__main__':
    if DEBUG:
        run("https://www.youtube.com/watch?v=r6cIKA1SWI8", "Spinning Sky Rabbit")
        exit(0)

    parser = argparse.ArgumentParser(
        description="Generate Anki flashcards from songs.",
        epilog="""Examples:
        Using Default lyrics.srt file:
        python main.py "https://www.youtube.com/watch?v=r6cIKA1SWI8" "Spinning Sky Rabbit"
        
        To specify srt path:
        python main.py "https://www.youtube.com/watch?v=r6cIKA1SWI8" "Spinning Sky Rabbit" -s .../.../mylyrics.srt""",
        formatter_class=argparse.RawDescriptionHelpFormatter  # This ensures that the epilog is formatted as provided
    )
    
    # Required arguments
    parser.add_argument("youtube_link", help="YouTube link of the song.")
    parser.add_argument("deck_name", help="Name of the Anki deck.")
    
    # Optional arguments
    parser.add_argument("-s", "--srt_path", default="ankifysong/lyrics.srt", help="Path to the SRT file. Default is ./lyrics.srt.")
    parser.add_argument("-o", "--output_path", default="ankifysong/data/anki_deck.apkg", help="Path to save the generated Anki deck. Default is ankifysong/data/anki_deck.apkg.")
    
    args = parser.parse_args()

    run(args.youtube_link, args.deck_name, args.srt_path, args.output_path)

