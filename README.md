# AnkifySong
Convert a song to an Anki Deck by providing timestamps and a YouTube URL.
This is primarily for the purpose of learning lyrics rather than learning word by word.


## Installation
Download dependencies:
`$ pip install -r requirements.txt`

Next, we need PyTorch for vocal-remover.
Uses https://github.com/tsurumeso/vocal-remover/blob/develop/README.md.

### Install PyTorch
**See**: [GET STARTED](https://pytorch.org/get-started/locally/)
For me the command was `$ pip3 install torch torchvision torchaudio` but it depends on your operating system/specific needs. Please see that link!

## Run it!
First let's 
Then, please run main.py.
`$ python3 main.py`
AnkifySong will separate the song into cards, with Audio Recordings, and create a new Anki deck.
