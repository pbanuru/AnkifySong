# AnkifySong
Convert a song to an Anki Deck by providing timestamps and a YouTube URL.
This is primarily for the purpose of learning lyrics rather than learning word by word.

To use, 
Enter the YouTube URL of the song you want to convert, into the first line of ```instructions.txt```
Then:
Describe each card in ```instructions.txt``` following the format shown in ```format.txt```
Modify ```format.txt``` as desired. The "Song Audio Period" field must not be removed, and must be last.

Ex. If format.txt is as follows:
```
Song Lyric
Song Lyric Romanized
Song Lyric Translation
Song Audio Period
```
Then the instructions.txt file should be as follows:
```
どうせならもう
Douse nara mou
If you know what you want to do
10.9-13.5

ヘタクソな夢を描いていこうよ
Hetakuso na yume wo egaite ikou yo
Sketch out your clumsy dreams
0:13.58-17.3

...
```

Then, please run main.py.
AnkifySong will separate the song into cards, with Audio Recordings, and create a new Anki deck.

I used Adobe Audition to gather the timestamps for extra accuracy.
I have not tried it, but Free software such as:
Media Player Classic (MPC-HC) might work, as you can see milliseconds in the timestamp.
https://superuser.com/questions/964808/video-player-that-shows-milliseconds

Alternatively, you can gather timestamps straight from YouTube, which shows only to the second.
