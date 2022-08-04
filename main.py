from ankify import *
import os


def run():
    deck = gen_deck("Anki Deck")
    model = gen_model("Anki Model")
    note = genanki.Note(model, ["What is the time?", "6:25PM"])
    deck.add_note(note)

    # Generate package
    genanki.Package(deck).write_to_file("data/anki_deck.apkg")


if __name__ == '__main__':
    run()
