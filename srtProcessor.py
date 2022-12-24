import srt
import mp3Processor
from datetime import timedelta

# Seconds before to subtract from start time and seconds after to add to end time of subtitle
BUFFER = 0.5

def add_remove_buffer(subtitle):
    '''
    Takes in a subtitle and adds a buffer to the start and end times.
    '''

    delta = timedelta(seconds=BUFFER)
    suggested_start = subtitle.start - delta
    suggested_end = subtitle.end + delta
    zero = timedelta(seconds=0)
    song_len = timedelta(seconds=mp3Processor.song_length())

    subtitle.start = suggested_start if suggested_start > zero else zero
    subtitle.end = suggested_end if suggested_end < song_len else song_len

    return subtitle

def processSrtFile(srt_file_path):
    '''
    Takes in a .srt file and generates two list data structures.

    # Note how for each note generation, we need to specify the fields of the model
    # As such, we need to generate a list of field lists, where each field list is a list of the fields for a single note
    note = genanki.Note(
        model, ["また月が昇る", "The moon is rising again", "[sound:mata0_src.mp3]", "[sound:mata0_vocals.mp3]"])
    deck.add_note(note)

    # Note how we need to specify the paths of each audio file that we want to include in the package
    # These paths will be used to locate the files specified in the fields of the notes (to my knowledge, I haven't looked into the genanki source code)
    # Generate package
    pkg = genanki.Package(deck, ["data/clips/mata0_src.mp3", "data/clips/mata0_vocals.mp3"])
    pkg.write_to_file("data/anki_deck.apkg")

    Where do these paths come from?
    We need to generate the song subclips and the isolated vocals for each srt subtitle,
    naming them according to first word of the english transliteration,
    followed by the index of the subtitle in the srt file.
    '''

    note_field_lists = []
    audio_paths = []

    with open(srt_file_path, "r", encoding="utf-8") as f:
        for i, subtitle in enumerate(srt.parse(f.read()), start=1):

            # Gather the fields of the current note
            content = subtitle.content.splitlines()
            foreign = content[0]
            transliteration = content[1]
            english = content[2]
            filename = f"{transliteration.split()[0]}{i}"

            # Add buffer to start and end times
            subtitle = add_remove_buffer(subtitle)

            # Generate the subclips for source audio and isolated vocals for each subtitle
            clip_src_name, clip_src_path, clip_vocals_name, clip_vocals_path = mp3Processor.clip_timestamp(subtitle.start.seconds, subtitle.end.seconds, filename)
            
            # Add the fields of the current note
            fields = [foreign, transliteration, english, f"[sound:{clip_src_name}]", f"[sound:{clip_vocals_name}]"]
            note_field_lists.append(fields)

            # Add to the list of audio paths
            audio_paths.append(clip_src_path)
            audio_paths.append(clip_vocals_path)

    return note_field_lists, audio_paths



if __name__ == '__main__':
    processSrtFile()