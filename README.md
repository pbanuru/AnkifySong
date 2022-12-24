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

## INSTALLATION
Download the repository.

Download the dependencies.
This project uses the following external libraries: genanki, pytube, moviepy, srt.
```
$ pip install -r requirements.txt
```

We also need to install PyTorch (used for vocal isolation)
**See**: [GET STARTED](https://pytorch.org/get-started/locally/)

Additionally, install the requirements from vocal-remover [vocal-remover](https://github.com/tsurumeso/vocal-remover/blob/develop/README.md)
```
$ cd vocal-remover/
$ pip install -r requirements.txt
```

## Run it!

