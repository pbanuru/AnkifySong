import genanki
import random



def rand_id():
    '''
    Note from https://github.com/kerrickstaley/genanki:

    Model:
    You need to pass a model_id so that Anki can keep track of your model. 
    It's important that you use a unique model_id for each Model you define. 
    Use import random; random.randrange(1 << 30, 1 << 31) 
    to generate a suitable model_id, and hardcode it into your Model definition.

    Deck:
    Once again, you need a unique deck_id that you should generate once 
    and then hardcode into your .py file.
    '''
    return random.randrange(1 << 30, 1 << 31)


def model_setup():
    fields = [
        {'name': 'Foreign Lyrics'},
        {'name': 'Transliterated Lyrics'},
        {'name': 'English Lyrics'},
        {'name': 'Source_Clip'},
        {'name': 'Vocals_Clip'},

    ]
    templates = [
        {
            'name': 'Song Template', 
            'qfmt': '{{Foreign Lyrics}}<br>Listen:{{Source_Clip}}', # qfmt is the question format (front side)
            'afmt': # afmt is the answer format (back side)
                '{{FrontSide}}<br>\
                Isolated Vocals:{{Vocals_Clip}}<br>\
                {{Transliterated Lyrics}}<br>\
                <hr id="answer">{{English Lyrics}}', 
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

def gen_package(deck, audio_paths):
    package = genanki.Package(deck, audio_paths)
    package.write_to_file("data/anki_deck.apkg")

def add_notes(deck, model, fields_list):
    '''
    Add all notes to the deck, given a list of field lists.

    The fields of the model specified in model_setup() detail how the note (flashcard) will be formatted
    '''
    for fields in fields_list:
        note = genanki.Note(model, fields)
        deck.add_note(note)
    return deck

