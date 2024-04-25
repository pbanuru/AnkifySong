import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from ankifysong.gui import AnkifySongGUI
import subprocess
import sys

class TestAnkifySongGUI(unittest.TestCase):
    def setUp(self):
        """Create an instance of the GUI before each test."""
        self.app = AnkifySongGUI()
        self.app.python_path = sys.executable

    def test_default_values_inserted(self):
        """Test if default values are correctly inserted into Entry widgets."""
        self.assertEqual(self.app.youtube_entry.get(), "https://www.youtube.com/watch?v=r6cIKA1SWI8")
        self.assertEqual(self.app.deck_entry.get(), "Spinning Sky Rabbit")
        self.assertEqual(self.app.srt_entry.get(), r".\lyrics.srt")
        self.assertEqual(self.app.output_entry.get(), r".\anki_deck.apkg")

    @patch('tkinter.filedialog.askopenfilename')
    def test_browse_srt(self, mock_askopenfilename):
        """Test the browse_srt method."""
        mock_askopenfilename.return_value = 'path/to/file.srt'
        self.app.browse_srt()
        self.assertEqual(self.app.srt_entry.get(), 'path/to/file.srt')

    @patch('tkinter.filedialog.asksaveasfilename')
    def test_browse_output(self, mock_asksaveasfilename):
        """Test the browse_output method."""
        mock_asksaveasfilename.return_value = 'path/to/output.apkg'
        self.app.browse_output()
        self.assertEqual(self.app.output_entry.get(), 'path/to/output.apkg')

    @patch('subprocess.Popen')
    @patch('tkinter.messagebox.showinfo')  # Patch the showinfo method
    def test_start_process(self, mock_showinfo, mock_popen):
        """Test the start_process method."""
        process_mock = MagicMock()
        attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock

        self.app.start_process()

        mock_popen.assert_called_with(
            [self.app.python_path, "main.py", "https://www.youtube.com/watch?v=r6cIKA1SWI8", "Spinning Sky Rabbit", "-s", r".\lyrics.srt", "-o", r".\anki_deck.apkg"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        self.assertIn('output', self.app.output_box.get('1.0', tk.END))
        mock_showinfo.assert_called_once()  # Ensure that showinfo was called

    def tearDown(self):
        """Destroy the GUI instance after each test."""
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
