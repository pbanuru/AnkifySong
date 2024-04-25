import pytube
import moviepy.editor as mp
import os
import shutil

class Song:
    """
    Song class to organize song data
    """

    def __init__(self, url):
        self.url = url
        self.download()
        self.isolate_vocals() # Remove vocals from source audio and generate audio_Vocals.wav and audio_Instruments.wav
        self.AUDIO_SRC_CLIP = mp.AudioFileClip("ankifysong/data/core/audio.aac")
        self.AUDIO_VOCALS_CLIP = mp.AudioFileClip("ankifysong/data/core/audio_Vocals.wav")

    def download(self):
        """
        Download song from Youtube URL
        """

        # Ensure the directory exists
        os.makedirs("ankifysong/data/core", exist_ok=True)

        # Check for existing audio file in data folder
        if os.path.exists("ankifysong/data/core/audio.aac"):
            print("Audio already downloaded")
            return

        yt = pytube.YouTube(self.url)
        title = yt.title

        print(f'Downloading {title} ...')

        # Download the file
        yt.streams.filter(only_audio=True).first().download(output_path="ankifysong/data/core", filename='audio.aac')

        print(f'Download Complete: {title} ✨')

    def isolate_vocals(self):

        # Check if vocal data/audio_Vocals.wav or data/audio_Instruments.wav exists
        if os.path.exists("ankifysong/data/core/audio_Vocals.wav") and os.path.exists("ankifysong/data/core/audio_Instruments.wav"):
            print("Vocals already extracted")
            return
            
        # Call vocal remover 
        print("Extracting Pure Vocals...")
        os.system("cd ankifysong/vocal-remover && python inference.py --input ../data/core/audio.aac --gpu 0")
        # subprocess.run(["cd", "vocal-remover", "&&", "python", "inference.py", "--input", "../data/core/audio.aac", "--gpu", "0"])
        
        # Move vocal-remover/audio_Vocals.wav to data/audio_Vocals.wav
        shutil.move("ankifysong/vocal-remover/audio_Vocals.wav", "ankifysong/data/core/audio_Vocals.wav")
        shutil.move("ankifysong/vocal-remover/audio_Instruments.wav", "ankifysong/data/core/audio_Instruments.wav")

    def clip_timestamp(self, start, end, filename):
        """
        Download a subclip of the audio file as an mp3, giving it the name filename.mp3
        """
        # Ensure the directory for clips exists
        os.makedirs("ankifysong/data/clips", exist_ok=True)

        # Use main audio file
        clip_src = self.AUDIO_SRC_CLIP.subclip(start, end)

        clip_src_name = f"{filename}_src.mp3"
        clip_src_path = f"ankifysong/data/clips/{clip_src_name}"
        clip_src.write_audiofile(clip_src_path)

        # Use vocals only
        clip_vocals = self.AUDIO_VOCALS_CLIP.subclip(start, end)

        clip_vocals_name = f"{filename}_vocals.mp3"
        clip_vocals_path = f"ankifysong/data/clips/{clip_vocals_name}"
        clip_vocals.write_audiofile(clip_vocals_path)

        return clip_src_name, clip_src_path, clip_vocals_name, clip_vocals_path

    def song_length(self):
        """
        Returns the length of the audio file in seconds
        """
        return self.AUDIO_SRC_CLIP.duration
        