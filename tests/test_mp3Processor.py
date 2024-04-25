import unittest
from unittest.mock import patch, MagicMock
from ankifysong.mp3Processor import Song

class TestSong(unittest.TestCase):
    @patch('ankifysong.mp3Processor.os.path.exists')
    @patch('ankifysong.mp3Processor.pytube.YouTube')
    def test_download(self, mock_youtube, mock_exists):
        # Test when file already exists
        mock_exists.return_value = True
        song = Song("dummy_url")
        song.download()
        mock_youtube.assert_not_called()

        # Test downloading new file
        mock_exists.return_value = False
        song.download()
        mock_youtube.assert_called_once_with("dummy_url")

    @patch('ankifysong.mp3Processor.os.path.exists')
    @patch('ankifysong.mp3Processor.shutil.move')
    @patch('ankifysong.mp3Processor.os.system')
    def test_isolate_vocals(self, mock_system, mock_move, mock_exists):
        # Test when vocals are already extracted
        mock_exists.return_value = True
        song = Song("dummy_url")
        song.isolate_vocals()
        mock_system.assert_not_called()

        # Test extracting vocals
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

        # Check if subclips are created and files are written
        self.assertEqual(mock_clip.write_audiofile.call_count, 2)

    @patch('ankifysong.mp3Processor.mp.AudioFileClip')
    def test_song_length(self, mock_audiofileclip):
        mock_clip = MagicMock()
        mock_clip.duration = 120
        mock_audiofileclip.return_value = mock_clip

        song = Song("dummy_url")
        length = song.song_length()

        self.assertEqual(length, 120)

if __name__ == '__main__':
    unittest.main()
