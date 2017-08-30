

import unittest
import os


def get_lyrics():
    pass


def create_wordcloud(wiki_url):
    pass


class TestBIAT(unittest.TestCase):
    def test_lyrics(self):
        """Test that a string gets return from get_lyrics()"""
        self.assertIsInstance(get_lyrics(), str)

    def test_wordcloud_creation(self):
        """Test that a new file is created when create_wordcloud() is called"""
        filecount_before = len(os.listdir())
        create_wordcloud('http://lyrics.wikia.com/wiki/The_Beatles:Lucy_In_The_Sky_With_Diamonds')
        self.assertEqual(filecount_before + 1, len(os.listdir()))
