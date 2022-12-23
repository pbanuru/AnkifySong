from ankify import *
import os
from time import sleep
import mp3Processor


def run():
    # # delete data/anki_deck.apkg if it exists
    # if os.path.exists("data/anki_deck.apkg"):
    #     os.remove("data/anki_deck.apkg")
    #     print("Deleted data/anki_deck.apkg")
    #     sleep(1)


    # Empty data folder of all files besides placeholder
    for file in os.listdir("data"):
        if file != "placeholder":
            os.remove(f"data/{file}")
    print(f"Emptied data/")
    
    mp3Processor.download("https://www.youtube.com/watch?v=r6cIKA1SWI8")
    mp3Processor.clip_timestamp(0, 5, "mata0")

    deck = gen_deck("Anki Deck")
    model = gen_model("Anki Model")

    # The fields of the model specified in model_setup() detail how the note (flashcard) will be formatted
    note = genanki.Note(
        model, ["また月が昇る", "The moon is rising again", "[sound:mata0.mp3]"])
    deck.add_note(note)

    # Generate package
    pkg = genanki.Package(deck, ["data/mata0.mp3"])
    pkg.write_to_file("data/anki_deck.apkg")


if __name__ == '__main__':
    run()
