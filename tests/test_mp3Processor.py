import unittest
from unittest.mock import patch, MagicMock
from ankifysong.mp3Processor import Song

class TestSong(unittest.TestCase):
    @patch('ankifysong.mp3Processor.os.path.exists')
    @patch('ankifysong.mp3Processor.pytube.YouTube')
    def test_download(self, mock_youtube, mock_exists):
        # Check that YouTube download is skipped if the file already exists.
        mock_exists.return_value = True
        song = Song("dummy_url")
        song.download()
        mock_youtube.assert_not_called()

        # Ensure YouTube's download method is called when the file does not exist.
        mock_exists.return_value = False
        song.download()
        mock_youtube.assert_called_once_with("dummy_url")

    @patch('ankifysong.mp3Processor.os.path.exists')
    @patch('ankifysong.mp3Processor.shutil.move')
    @patch('ankifysong.mp3Processor.os.system')
    def test_isolate_vocals(self, mock_system, mock_move, mock_exists):
        # Verify no action is taken if the vocals have already been isolated.
        mock_exists.return_value = True
        song = Song("dummy_url")
        song.isolate_vocals()
        mock_system.assert_not_called()

        # Check that the system command for isolating vocals is executed when they are not already isolated.
        mock_exists.return_value = False
        song.isolate_vocals()
        mock_system.assert_called_once()

    @patch('ankifysong.mp3Processor.mp.AudioFileClip')
    def test_clip_timestamp(self, mock_audiofileclip):
        mock_clip = MagicMock()
        mock_audiofileclip.return_value = mock_clip
        mock_clip.subclip.return_value = mock_clip
        mock_clip.write_audiofile = MagicMock()

        song = Song("dummy_url")
        song.clip_timestamp(0, 10, "test_clip")

        # Test clipping a segment of the song and writing it to a file, ensuring the write operation is called twice.
        self.assertEqual(mock_clip.write_audiofile.call_count, 2)

    @patch('ankifysong.mp3Processor.mp.AudioFileClip')
    def test_song_length(self, mock_audiofileclip):
        mock_clip = MagicMock()
        mock_clip.duration = 120
        mock_audiofileclip.return_value = mock_clip

        song = Song("dummy_url")
        length = song.song_length()

        # Verify that the song length is correctly retrieved from the audio clip.
        self.assertEqual(length, 120)

if __name__ == '__main__':
    unittest.main()
