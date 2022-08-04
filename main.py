from ankify import *
import os
from time import sleep


def run():
    # delete data/anki_deck.apkg if it exists
    if os.path.exists("data/anki_deck.apkg"):
        os.remove("data/anki_deck.apkg")
        print("Deleted data/anki_deck.apkg")
        sleep(1)

    deck = gen_deck("Anki Deck")
    model = gen_model("Anki Model")
    note = genanki.Note(
        model, ["What is the time?", "6:25PM", "[sound:sound_Tsurai_18.mp3]"])
    deck.add_note(note)

    # Generate package
    pkg = genanki.Package(deck, ["data/sound_Tsurai_18.mp3"])
    pkg.write_to_file("data/anki_deck.apkg")


if __name__ == '__main__':
    run()
