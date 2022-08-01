from pytube import YouTube


def download_video(url):
    yt = YouTube(url)
    yt.streams.filter(only_audio=True).first().download(
        filename='data/audio.aac')


if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=RP8Dhn3lQgE"
    download_video(url)
    print("Download complete")
