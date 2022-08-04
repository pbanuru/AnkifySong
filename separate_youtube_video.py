from re import sub
from pytube import YouTube
from moviepy.audio.AudioClip import AudioClip
from moviepy.editor import AudioFileClip


def download_audio(url):
    yt = YouTube(url)
    yt.streams.filter(only_audio=True).first().download(
        filename='data/audio.aac')


def get_src_audio(url):
    download_audio(url)
    return AudioFileClip('data/audio.aac')


def get_audio_name(word, card_number):
    return f'data/sound_{word}_{card_number}.mp3', f'sound_{word}_{card_number}.mp3'


def audio_clip(timestamps, src_audio, name, card_number):
    start, end = timestamps.split('-')
    subclip = src_audio.subclip(start, end)
    output_path, output_basename = get_audio_name(name, card_number)
    print(f'Saving {output_path}')
    subclip.write_audiofile(output_path)

    return output_path, output_basename


if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=RP8Dhn3lQgE"
    download_audio(url)
    print("Download complete")
