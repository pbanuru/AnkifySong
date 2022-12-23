# This module will download a specified file from a specified URL using pytube

import pytube
import moviepy.editor as mp



def download(url):
    """
    Download song from Youtube URL
    """
    yt = pytube.YouTube(url)
    title = yt.title

    print(f'Downloading {title} ...')

    # Download the file
    yt.streams.filter(only_audio=True).first().download(
        filename='data/audio.aac')

    print(f'Download Complete: {title} ✨')

def clip_timestamp(start, end, filename):
    """
    Download a subclip of the audio file as an mp3, giving it the name filename.mp3
    """
    clip = mp.AudioFileClip("data/audio.aac")
    clip = clip.subclip(start, end)
    clip.write_audiofile(f"data/{filename}.mp3")