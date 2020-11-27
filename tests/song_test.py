import unittest

from classes.guests import Guests
from classes.rooms import Rooms
from classes.songs import Songs


class TestSongs(unittest.TestCase):
    def setUp(self):
        self.song_1 = Songs("Kings Of Leon", "Charmer", 4)
        self.song_2 = Songs("Arctic Monkeys", "Flourecent Adolescent", 3)
        self.song_3 = Songs("Jay-Z", "Empire State Of Mind", 5)
        self.song_4 = Songs("Chance The Rapper", "Acid Rap", 5)

    def test_song_has_artist(self):
        self.assertEqual("Kings Of Leon", self.song_1.artist)
