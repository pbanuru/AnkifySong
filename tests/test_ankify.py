import unittest
from unittest.mock import patch
from ankifysong.ankify import rand_id, model_setup, gen_model, gen_deck, gen_package, add_notes
import genanki

class TestAnkify(unittest.TestCase):
    def setUp(self):
        """Common setup data for the tests."""
        self.title = "Test Model"
        self.deck_title = "Test Deck"

    def test_rand_id_generates_valid_id(self):
        """Ensure rand_id returns an ID within the specified range."""
        id = rand_id()
        self.assertTrue(1 << 30 <= id < 1 << 31, "ID should be within the 30-bit range.")

    def test_model_setup_returns_correct_structure(self):
        """Check that model_setup returns the correct number of fields and templates."""
        fields, templates = model_setup()
        self.assertEqual(len(fields), 6, "Should have exactly 6 fields.")
        self.assertEqual(len(templates), 1, "Should have exactly 1 template.")

    def test_gen_model_creates_model_with_correct_title(self):
        """Ensure gen_model creates a model with the specified title and correct structure."""
        model = gen_model(self.title)
        self.assertEqual(model.name, self.title, "Model title should match the input title.")
        self.assertTrue(isinstance(model, genanki.Model), "Should be an instance of genanki.Model.")

    def test_gen_deck_creates_deck_with_correct_title(self):
        """Ensure gen_deck creates a deck with the specified title."""
        deck = gen_deck(self.deck_title)
        self.assertEqual(deck.name, self.deck_title, "Deck title should match the input title.")
        self.assertTrue(isinstance(deck, genanki.Deck), "Should be an instance of genanki.Deck.")

    @patch('genanki.Package.write_to_file')
    def test_gen_package_calls_write_to_file_once(self, mock_write_to_file):
        """Test that gen_package correctly calls write_to_file exactly once."""
        deck = genanki.Deck(123, self.deck_title)
        gen_package(deck, [], "output.apkg")
        mock_write_to_file.assert_called_once_with("output.apkg")

    def test_add_notes_adds_correct_number_of_notes(self):
        """Verify that add_notes correctly adds notes to the deck."""
        deck = genanki.Deck(123, self.deck_title)
        model = gen_model(self.title)
        fields_list = [[{"name": "value"}] * 6]  # Simulate one note with 6 fields
        deck = add_notes(deck, model, fields_list)
        self.assertEqual(len(deck.notes), 1, "Should add exactly one note to the deck.")

if __name__ == '__main__':
    unittest.main()
