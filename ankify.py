import genanki
import random


def rand_id():
    return random.randrange(1 << 30, 1 << 31)


def model_setup():
    fields = [{'name': 'Question'}, {'name': 'Answer'}]
    templates = [
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ]
    return fields, templates


def gen_model(title):
    model_id = rand_id()
    fields, template = model_setup()
    model = genanki.Model(model_id, title, fields, template)
    return model


def gen_deck(title):
    deck_id = rand_id()
    return genanki.Deck(deck_id, title)
