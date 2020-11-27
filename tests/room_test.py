import unittest

from classes.guests import Guests
from classes.rooms import Rooms
from classes.songs import Songs


class TestRooms(unittest.TestCase):
    def setUp(self):
        self.room_1 = Rooms("Red", 60, 30, 25)
        self.room_2 = Rooms("Yellow", 30, 15, 10)
        self.room_3 = Rooms("Green", 45, 20, 15)
        self.room_4 = Rooms("Blue", 60, 25, 10)
        self.room_5 = Rooms("Orange", 10, 5, 4)

        self.guest_1 = Guests("Ann", 50, 45)
        self.guest_2 = Guests("Bill", 40, 35)
        self.guest_3 = Guests("Carl", 30, 18)
        self.guest_4 = Guests("Dee", 15, 17)

        self.song_1 = Songs("Kings Of Leon", "Charmer", 4)
        self.song_2 = Songs("Arctic Monkeys", "Flourecent Adolescent", 3)
        self.song_3 = Songs("Jay-Z", "Empire State Of Mind", 5)
        self.song_4 = Songs("Chance The Rapper", "Acid Rap", 5)


# basic test assuring class set up correctly


    def test_room_has_name(self):
        self.assertEqual("Red", self.room_1.name)

    def test_room_has_time_limit(self):
        self.assertEqual(30, self.room_2.time_limit)

    def test_room_has_price(self):
        self.assertEqual(20, self.room_3.price)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room_4.capacity)

    def test_room_playlist_empty(self):
        self.assertEqual([], self.room_1.playlist)

    def test_room_cash_starts_at_0(self):
        self.assertEqual(0, self.room_2.cash)

    def test_room_num_guests_starts_at_0(self):
        self.assertEqual(0, self.room_3.num_guests)

    def test_add_guest_to_room(self):
        group = [self.guest_4]
        self.room_4.add_guest(group)
        self.assertEqual(1, self.room_4.num_guests)

    def test_add_song_to_playlist(self):
        self.room_1.add_song_to_playlist(self.song_1)
        self.assertEqual(1, len(self.room_1.playlist))

    def test_can_remove_song_from_playlist(self):
        self.room_1.remove_song_from_playlist(self.song_1)
        self.assertEqual([], self.room_1.playlist)
