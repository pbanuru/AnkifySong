# This module will download a specified file from a specified URL using pytube

import pytube
import moviepy.editor as mp
import os
import shutil


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

def isolate_vocals():

    # Check if vocal data/audio_Vocals.wav or data/audio_Instruments.wav exists
    if os.path.exists("data/core/audio_Vocals.wav") and os.path.exists("data/core/audio_Instruments.wav"):
        print("Vocals already extracted")
        return
        
    # Call vocal remover 
    print("Extracting Pure Vocals...")
    os.system("cd vocal-remover && python3 inference.py --input ../data/core/audio.aac --gpu 0")
    
    # Move vocal-remover/audio_Vocals.wav to data/audio_Vocals.wav
    shutil.move("vocal-remover/audio_Vocals.wav", "data/core/audio_Vocals.wav")
    shutil.move("vocal-remover/audio_Instruments.wav", "data/core/audio_Instruments.wav")

def clip_timestamp(start, end, filename):
    """
    Download a subclip of the audio file as an mp3, giving it the name filename.mp3
    """
    # Use main audio file
    clip_src = mp.AudioFileClip("data/core/audio.aac")
    clip_src = clip_src.subclip(start, end)

    clip_src_name = f"{filename}_src.mp3"
    clip_src_path = f"data/clips/{clip_src_name}"
    clip_src.write_audiofile(clip_src_path)

    # Use vocals only
    clip_vocals = mp.AudioFileClip("data/core/audio_Vocals.wav")
    clip_vocals = clip_vocals.subclip(start, end)

    clip_vocals_name = f"{filename}_vocals.mp3"
    clip_vocals_path = f"data/clips/{clip_vocals_name}"
    clip_vocals.write_audiofile(clip_vocals_path)

    return clip_src_name, clip_src_path, clip_vocals_name, clip_vocals_path



    