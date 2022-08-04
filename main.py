from ankify import *
from separate_youtube_video import *
import os


def MissingFieldException(expected_field, line_number):
    raise Exception(
        "Expected field: " +
        expected_field + " at line " + str(line_number)
    )


def expected_card_count():
    '''
    field_count is the number of distinct fields per card.
    We expect one card to be made for every (field_count+1) lines in instructions.txt (Excluding the song URL and blank space at lines 1 and 2)
    This includes the fields, and the blank line after each set of fields.
    '''

    with open("instructions.txt", 'r', encoding='utf-8') as f:
        instructions_line_count = len(f.readlines())-2

    field_count = len(format_list())

    if field_count == 0:
        raise Exception("No fields found in format.txt")
    if (instructions_line_count % (field_count+1)) != 0:
        print("Instructions.txt has an incorrect number of lines")

    return instructions_line_count // (field_count+1)


def instruction_reader(model_title, deck_title):
    '''
    Iterate through instructions.txt and generate cards along with audio media clips.
    Follow the format in format.txt to label the data properly.
    '''
    mp3_files = []
    model = gen_model(model_title)
    deck = gen_deck(deck_title)
    expected_cards_count = expected_card_count()

    with open('instructions.txt', 'r', encoding='utf-8') as f:
        line_number = 1
        card_num = 0
        while True:
            if line_number == 1:
                URL = f.readline().strip()
                src_audio = get_src_audio(URL)
                f.readline()
                line_number += 2
                continue

            if card_num == expected_cards_count:
                break

            fields = []
            for i in range(len(format_list())):
                field = f.readline().strip()
                line_number += 1
                if not field:
                    if len(fields) == 0:
                        break  # end of file
                    else:
                        MissingFieldException(format_list()[i], line_number)

                if i == len(format_list())-1:
                    # Last field holds the lyrics timestamps, we must get the relevant audio clip.
                    output_path, output_basename = audio_clip(
                        # For the name field, we use the first word of the romanized lyrics; though you can choose anything for name- cards_added will give us unique clip filenames.
                        field, src_audio, fields[-2].split()[0], card_num
                    )
                    mp3_files.append(output_path)
                    fields.append(output_basename)
                else:
                    fields.append(field)

            deck.add_note(gen_note(model, fields))
            print(f"Added card {fields[-3].split()[0]}_{card_num}")
            card_num += 1

            blank_line = f.readline()
            line_number += 1
            if not (blank_line == "\n"):
                raise Exception(
                    "Missing blank line at line " + str(line_number)
                )

    print(f'Deck {deck_title} created successfully!')
    print(f'{card_num} cards added to deck')

    return deck, mp3_files


def run():
    model_title, deck_title = "Japanese Lyrics", "Ketsui No Asa Ni"
    deck, mp3_files = instruction_reader(model_title, deck_title)
    gen_package(deck, mp3_files, f'data/{deck_title}.apkg')
    print("Package generated successfully!")

    if input("Delete mp3 files? (Y/n) ") in ['Y', 'y', '']:
        for mp3_file in mp3_files:
            os.remove(mp3_file)
        print("MP3 files deleted successfully!")


if __name__ == '__main__':
    run()
