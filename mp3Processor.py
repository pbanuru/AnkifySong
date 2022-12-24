# This module will download a specified file from a specified URL using pytube

import pytube
import moviepy.editor as mp
import os


def download(url):
    """
    Download song from Youtube URL
    """

    # Check for existing audio file in data folder
    if os.path.exists("data/core/audio.aac"):
        print("Audio already downloaded")
        return

    yt = pytube.YouTube(url)
    title = yt.title

    print(f'Downloading {title} ...')

    # Download the file
    yt.streams.filter(only_audio=True).first().download(
        filename='data/core/audio.aac')

    print(f'Download Complete: {title} ✨')

def clip_timestamp(start, end, filename):
    """
    Download a subclip of the audio file as an mp3, giving it the name filename.mp3
    """
    # Use main audio file
    clip_src = mp.AudioFileClip("data/core/audio.aac")
    clip_src = clip_src.subclip(start, end)
    clip_src.write_audiofile(f"data/clips/{filename}_src.mp3")

    # Use vocals only
    clip_vocals = mp.AudioFileClip("data/core/audio_Vocals.wav")
    clip_vocals = clip_vocals.subclip(start, end)
    clip_vocals.write_audiofile(f"data/clips/{filename}_vocals.mp3")



    