import unittest

from translator import english_to_french, french_to_english


class TranslatorTests(unittest.TestCase):
    def test_french_to_english_translation_hello(self):
        english_text = "Hello"
        expected_result = "Bonjour"
        result = english_to_french(english_text)
        self.assertEqual(result, expected_result)

    def test_english_to_french_translation_bonjour(self):
        french_text = "Bonjour"
        expected_result = "Hello"
        result = french_to_english(french_text)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
