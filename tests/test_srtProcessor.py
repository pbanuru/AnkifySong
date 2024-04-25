import unittest
from ankifysong.srtProcessor import SrtProcessor
from unittest.mock import Mock, mock_open, patch
from datetime import timedelta
import srt

class TestSrtProcessor(unittest.TestCase):
    # Test initialization of SrtProcessor to ensure it correctly stores its parameters
    def test_initialization(self):
        song_mock = Mock()
        song_mock.song_length.return_value = 300  # Mock song length as 300 seconds
        processor = SrtProcessor(song=song_mock, srt_file_path="path/to/file.srt", BUFFER=0.5)
        self.assertEqual(processor.song, song_mock)
        self.assertEqual(processor.srt_file_path, "path/to/file.srt")
        self.assertEqual(processor.BUFFER, 0.5)

    # Test the add_remove_buffer method to check if it correctly adjusts subtitle timings
    def test_add_remove_buffer(self):
        song_mock = Mock()
        song_mock.song_length.return_value = 300
        processor = SrtProcessor(song=song_mock, srt_file_path="", BUFFER=0.5)
        subtitle = srt.Subtitle(index=1, start=timedelta(seconds=10), end=timedelta(seconds=20), content="Test")
        processed_subtitle = processor.add_remove_buffer(subtitle)
        self.assertEqual(processed_subtitle.start, timedelta(seconds=9.5))
        self.assertEqual(processed_subtitle.end, timedelta(seconds=20.5))

    # Test the processSrtFile method to ensure it processes the SRT file and generates correct note fields and audio paths
    def test_process_srt_file(self):
        song_mock = Mock()
        song_mock.song_length.return_value = 300
        song_mock.clip_timestamp.return_value = ("src_name.mp3", "src_path.mp3", "vocals_name.mp3", "vocals_path.mp3")
        processor = SrtProcessor(song=song_mock, srt_file_path="path/to/file.srt", BUFFER=0.5)
        
        # Mock reading from a file and check if the processing of the file is correct
        with patch('builtins.open', mock_open(read_data="1\n00:00:10,000 --> 00:00:20,000\nTest\nTransliteration\nEnglish\n")):
            note_fields, audio_paths = processor.processSrtFile()
            self.assertEqual(len(note_fields), 1)  # Check if one note is created
            self.assertEqual(len(audio_paths), 2)  # Check if two audio paths are returned
            self.assertIn("src_path.mp3", audio_paths)  # Check if the source path is correct
            self.assertIn("vocals_path.mp3", audio_paths)  # Check if the vocals path is correct

if __name__ == '__main__':
    unittest.main()
