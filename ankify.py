import genanki
import random


def format_list():
    '''
    Store the format name-fields in a list.
    '''
    format = []
    with open('format.txt', 'r') as f:
        for line in f:
            format.append(line.strip())
    return format


def get_template():
    template = {}
    # Front template: (qfmt meaning question format)
    qfmt = '<h2>"{{Song Lyric}}"</h2>\
            <br>\
            {{Song Audio}}'
    # Back template: (afmt meaning answer format)
    # FrontSide repeats whatever is in the Front template (qfmt)
    afmt = '{{FrontSide}}\
            <hr id="answer">\
            <strong>{{Song Lyric Translation}}</strong>\
            <br><br>\
            {{Song Lyric Romanized}}'

    template['qfmt'] = qfmt
    template['afmt'] = afmt

    return template


def model_setup():
    format = format_list()
    field_list = format[:-1].append("Song Audio")
    fields = [{'name': field for field in field_list}]
    templates = [get_template()]
    return fields, templates


def rand_id():
    return random.randrange(1 << 30, 1 << 31)


def gen_model(title):
    model_id = rand_id()
    fields, templates = model_setup()

    model = genanki.Model(
        model_id,
        title,
        fields=fields,
        templates=templates
    )

    return model


def gen_deck(model_title, deck_title):
    deck_id = rand_id()
    model = gen_model(model_title)
    deck = genanki.Deck(deck_id, deck_title)
    return deck, model


def gen_note(model, fields):
    note = genanki.Note(
        model=model,
        fields=fields
    )
    return note
