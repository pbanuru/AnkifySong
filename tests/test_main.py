import unittest
from unittest.mock import patch, mock_open, Mock
import ankifysong.main as main


class TestClearData(unittest.TestCase):
    @patch('os.listdir')
    @patch('os.remove')
    def test_clear_data(self, mock_remove, mock_listdir):
        mock_listdir.side_effect = [
            ['file1.mp3', '.placeholder'],  # core directory
            ['clip1.mp3', '.placeholder'],  # clips directory
            ['anki_deck.apkg', 'core', 'clips']  # data directory
        ]

        main.REDOWNLOAD_CORE = True
        main.clear_data()

        # Check if the correct files are attempted to be removed
        mock_remove.assert_any_call('ankifysong/data/core/file1.mp3')
        mock_remove.assert_any_call('ankifysong/data/clips/clip1.mp3')
        mock_remove.assert_any_call('ankifysong/data/anki_deck.apkg')
        self.assertEqual(mock_remove.call_count, 3)

@patch('ankifysong.main.ankify')
@patch('ankifysong.main.srtProcessor.SrtProcessor')
@patch('ankifysong.main.mp3Processor.Song')
@patch('ankifysong.main.clear_data')
class TestRunFunction(unittest.TestCase):
    def test_run(self, mock_clear_data, mock_song, mock_srt_processor, mock_ankify):
        mock_song.return_value = Mock()
        mock_srt_processor_instance = Mock()
        mock_srt_processor.return_value = mock_srt_processor_instance
        mock_srt_processor_instance.processSrtFile.return_value = (['note1'], ['path1'])

        main.run("dummy_link", "dummy_name")

        # Validate that clear_data was called
        mock_clear_data.assert_called_once()

        # Validate interactions with ankify module
        mock_ankify.gen_deck.assert_called_once_with("dummy_name")
        mock_ankify.gen_model.assert_called_once_with("My Model")
        mock_ankify.add_notes.assert_called_once()
        mock_ankify.gen_package.assert_called_once()

if __name__ == '__main__':
    unittest.main()
