import unittest
from unittest.mock import patch, mock_open, Mock
import ankifysong.main as main


class TestClearData(unittest.TestCase):
    """
    TestClearData tests the functionality of the clear_data method in the main module.
    It checks if the method correctly identifies and removes the appropriate files when
    REDOWNLOAD_CORE is set to True.
    """
    @patch('os.listdir')
    @patch('os.remove')
    def test_clear_data(self, mock_remove, mock_listdir):
        # Setup mock responses for os.listdir to simulate different directory contents
        mock_listdir.side_effect = [
            ['file1.mp3', '.placeholder'],  # Simulate files in the core directory
            ['clip1.mp3', '.placeholder'],  # Simulate files in the clips directory
            ['anki_deck.apkg', 'core', 'clips']  # Simulate files in the data directory
        ]

        main.REDOWNLOAD_CORE = True
        main.clear_data()

        # Verify if the correct files are attempted to be removed based on the method logic
        mock_remove.assert_any_call('ankifysong/data/core/file1.mp3')
        mock_remove.assert_any_call('ankifysong/data/clips/clip1.mp3')
        mock_remove.assert_any_call('ankifysong/data/anki_deck.apkg')
        self.assertEqual(mock_remove.call_count, 3)

class TestRunFunction(unittest.TestCase):
    """
    TestRunFunction tests the run function in the main module. It ensures that all components
    involved in processing and generating an Anki deck are invoked correctly, and that the
    clear_data function is called as expected.
    """
    @patch('ankifysong.main.ankify')
    @patch('ankifysong.main.srtProcessor.SrtProcessor')
    @patch('ankifysong.main.mp3Processor.Song')
    @patch('ankifysong.main.clear_data')
    def test_run(self, mock_clear_data, mock_song, mock_srt_processor, mock_ankify):
        # Setup mock instances and return values for dependencies
        mock_song.return_value = Mock()
        mock_srt_processor_instance = Mock()
        mock_srt_processor.return_value = mock_srt_processor_instance
        mock_srt_processor_instance.processSrtFile.return_value = (['note1'], ['path1'])

        main.run("dummy_link", "dummy_name")

        # Check if clear_data was called as expected
        mock_clear_data.assert_called_once()

        # Validate interactions with the ankify module to ensure deck generation process
        mock_ankify.gen_deck.assert_called_once_with("dummy_name")
        mock_ankify.gen_model.assert_called_once_with("My Model")
        mock_ankify.add_notes.assert_called_once()
        mock_ankify.gen_package.assert_called_once()

if __name__ == '__main__':
    unittest.main()
