# AnkifySong
Are you trying to learn language through song?
Classic Flashcards have no audio in them, just words; and what's the most recognizable thing about lyrics?
It's the way they sound, the words are accomplices.

(This might explain why I like listening to BTS's songs, despite not knowing the meanings/messages of 70% of them.)

Anki flashcards can contain anything a website can; that includes audio.
We can use these to contain our sound, but the process of manually creating specialized Anki Decks is quite lengthy.

AnkifySong automatically creates subclips of the full song to put on each flashcard, each subclip showcasing the audio of that flashcard's phrase.
Additionally, it isolates the vocals on the back of each flashcard, in case you want to hone in on the pronounciation, without the background noise.

# REQUIRES
An srt (SubRip File Format) file, specifying the following for each flashcard:
start time of lyric phrase --> end time of lyric phrase,
foreign language lyrics,
english transliteration lyrics,
english translation lyrics

Ex:
```
1
00:00:00,618 --> 00:00:04,620
また月が昇る
mata tsuki ga noboru
The moon is rising again,

2
00:00:04,621 --> 00:00:08,825
今日が終わりだす
kyou ga owaridasu
and today is beginning to end

.
.
.
```

## INSTALLATION
Download the repository.

Download the dependencies.
This project uses the following external libraries: genanki, pytube, moviepy, srt.
```
$ pip install -r requirements.txt
```

We also need to install PyTorch (used for vocal isolation)
**See**: [GET STARTED](https://pytorch.org/get-started/locally/)

Additionally, install the requirements from [vocal-remover](https://github.com/tsurumeso/vocal-remover/blob/develop/README.md)

Please take a look at this repo if you need to understand how to modify the vocal isolation. Ex. change from gpu to cpu ML, etc.
```
$ cd vocal-remover/
$ pip install -r requirements.txt
```

## Run it!
Usage: `python3 main.py "<youtube-link>" "<deck-name>" [<srt-path>]`

Using Default lyrics.srt file:
`$ python3 main.py "https://www.youtube.com/watch?v=r6cIKA1SWI8" "Spinning Sky Rabbit"`
To specify srt path:
`$ python3 main.py "https://www.youtube.com/watch?v=r6cIKA1SWI8" "Spinning Sky Rabbit" .../.../mylyrics.srt`

If you dont specify the srt path, AnkifySong will use the lyrics.srt file in the source directory. By default, it contains the srt file to the song "回る空うさぎ" (Spinning Sky Rabbit).

When all is finished, load `data/anki_deck.apkg` into Anki, and you have your deck!

Card Front:
<img width="359" alt="image" src="https://user-images.githubusercontent.com/55062649/209429700-a85522e6-cfc4-4a08-804d-3739071e1cd9.png">
Card Back:
<img width="411" alt="image" src="https://user-images.githubusercontent.com/55062649/209429767-b68639e6-3897-407e-bcce-9ea6830566c6.png">

The design isn't the prettiest right now,

## Modifications (READ THIS)

### Design is Ugly ?
If you want to modify your card design, you can do that in `ankify.py:model_setup()`

### Lengthy Runtime ?
The first thing AnkifySong will do is download the song from the specified YouTube link, and extract the vocals. This is a time-consuming process, so if you find yourself calling main.py on the same song, head to `main.py` and modify the global variable `REDOWNLOAD_CORE`,
changing `REDOWNLOAD_CORE = True` to `REDOWNLOAD_CORE = False` to avoid reprocessing things that will not change.

On the other hand, if you are using many different songs/srt-files, keep this at `True` so that the old data is cleared when the script is called.

### SRT timings are too close to the start/ends of phrases ?
Head to `srtProcessor.py` and modify the `BUFFER` global variable, indicating the seconds (a float) to subtract from the start of each "subtitle phrase" and to add to the end of each.
I have set it to 0.5 seconds since that's what works for me.













