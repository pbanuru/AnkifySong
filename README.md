# AnkifySong
Are you trying to learn language through song?
Classic Flashcards have no audio in them, just words; and what's the most recognizable thing about lyrics?
It's the way they sound, the words are accomplices.

<img src="https://user-images.githubusercontent.com/55062649/209430434-c07adade-b99c-4abf-ba7c-2859b5334107.png" width="10%">
Anki flashcards can contain anything a website can; that includes audio.
We can use these to contain our sound, but the process of manually creating specialized Anki Decks is quite lengthy.

AnkifySong automatically creates subclips of the full song to put on each flashcard, each subclip showcasing the audio of that flashcard's phrase.
Additionally, it isolates the vocals on the back of each flashcard, in case you want to hone in on the pronounciation, without the background noise.

## REQUIRES
An srt (SubRip File Format) file, specifying the following for each flashcard:


```
number
start time of lyric phrase --> end time of lyric phrase,
foreign language lyrics,
english transliteration lyrics,
english translation lyrics
[optional annotation, see `lyrics_annotated.srt`]
```


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
$ cd ankifysong/
$ pip install -r requirements.txt
```

We also need to install PyTorch (used for vocal isolation)
[Setup](https://pytorch.org/get-started/locally/)

Additionally, install the requirements from [vocal-remover](https://github.com/tsurumeso/vocal-remover/blob/develop/README.md)

Please take a look at this repo if you need to understand how to modify the vocal isolation. Ex. change from gpu to cpu ML, etc.
Otherwise, as far as vocal-remover requirements are concerned, install them like this:
```
$ cd ankifysong/vocal-remover/
$ pip install -r requirements.txt
```

## Run it!
Usage: `python ankifysong/main.py "<youtube-link>" "<deck-name>" [<srt-path>]`

Using Default lyrics.srt file:
`$ python ankifysong/main.py "https://www.youtube.com/watch?v=r6cIKA1SWI8" "Spinning Sky Rabbit"`
To specify srt path:
`$ python ankifysong/main.py "https://www.youtube.com/watch?v=r6cIKA1SWI8" "Spinning Sky Rabbit" .../.../mylyrics.srt`
Ex. Feel free to try this out, lyrics_annotated.srt is provided.
`python ankifysong/main.py "https://www.youtube.com/watch?v=r6cIKA1SWI8" "Spinning Sky Rabbit" lyrics_annotated.srt`

If you dont specify the srt path, AnkifySong will use the lyrics.srt file in the ankifysong directory. By default, it contains the srt file to the song "回る空うさぎ" (Spinning Sky Rabbit).

When all is finished, load `ankifysong/data/anki_deck.apkg` into Anki, and you have your deck!

Card Front:
<img width="359" alt="image" src="https://user-images.githubusercontent.com/55062649/209429700-a85522e6-cfc4-4a08-804d-3739071e1cd9.png">

Card Back:
<img width="411" alt="image" src="https://user-images.githubusercontent.com/55062649/209429767-b68639e6-3897-407e-bcce-9ea6830566c6.png">

The design isn't the prettiest right now,

## Modifications (READ THIS)

### Design is Ugly ?
If you want to modify your card design, you can do that in `ankifysong/ankify.py:model_setup()`
<img width="786" alt="image" src="https://user-images.githubusercontent.com/55062649/209430407-9b676d37-4824-43f1-99f3-e6e111dca941.png">

### Lengthy Runtime ?
<img width="215" alt="image" src="https://user-images.githubusercontent.com/55062649/209430385-a29b2804-3c3b-4fa6-8c50-c64e5cd3046d.png">
The first thing AnkifySong will do is download the song from the specified YouTube link, and extract the vocals. This is a time-consuming process, so if you find yourself calling main.py on the same song, head to `ankifysong/main.py` and modify the global variable `REDOWNLOAD_CORE`,
changing `REDOWNLOAD_CORE = True` to `REDOWNLOAD_CORE = False` to avoid reprocessing things that will not change.

On the other hand, if you are using many different songs/srt-files, keep this at `True` so that the old data is cleared when the script is called.

### SRT timings are too close to the start/ends of phrases ?
<img width="555" alt="image" src="https://user-images.githubusercontent.com/55062649/209452349-ce4f5dab-5dd8-4744-b715-834626761d67.png">
Head to `main.py:run()` and modify the `buffer` argument in the srtProcessor Object initialization, indicating the seconds (a float) to subtract from the start of each "subtitle phrase" and to add to the end of each.
I have set it to 0.5 seconds since that's what works for me.

## Suggestions on getting SRT file

The format of an SRT file is quite simple, as you can see above. However, putting that together manually can be incredibly time intensive.

This is not necessarily a bad thing. We are trying to learn this song, so by manually going through the song, and typing the lyrics/translations, we can make strides towards learning the meanings of the words and phrases.

Alternatively, if your video is on YouTube, and already contains custom subtitles (You can **probably** trust the quality if they are custom),
You can use tools such as https://downsub.com/, to get an SRT. DownSub allows to create bilingual SRTs, so in the case someone has already created say, English, and Japanese subtitles for your song, all you need to do now is manually gather and add the English Transliteration. 

For Japanese, there are tools like http://www.romajidesu.com/translator/, or you can find transliterations on lyric sites, like [https://vocaloidlyrics.fandom.com/wiki/回る空うさぎ_(Mawaru_Sora_Usagi)](https://vocaloidlyrics.fandom.com/wiki/%E5%9B%9E%E3%82%8B%E7%A9%BA%E3%81%86%E3%81%95%E3%81%8E_(Mawaru_Sora_Usagi))

[Kapwing Online Tool](https://www.kapwing.com/studio/editor) seems like a good tool for creating SRTs from scratch.

## Learning Tips
Add notes to your cards, see `ankifysong/lyrics_annotated.srt` in comparison to `ankifysong/lyrics.srt`.
This can provide more information as to meaning, and can decrease the need to back and forth translate things.
I find ChatGPT to be an awesome tool to write lyric phrase explanations. That's what I used for `ankifysong/lyrics_annotated.srt`. 
The GPT Api can also be used to programmatically write explanations! I haven't added this feature yet. If you want to, please make a PR!
