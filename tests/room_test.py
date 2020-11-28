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

        self.guest_1 = Guests("Ann", 50, 45, {"Kings Of Leon": "Charmer"})
        self.guest_2 = Guests("Bill", 40, 35, {
                              "Arctic Monkeys": "Flourecent Adolescent"})
        self.guest_3 = Guests("Carl", 30, 18, {
                              "Jay-Z": "Empire State Of Mind"})
        self.guest_4 = Guests("Dee", 5, 17, {"Chance The Rapper": "Acid Rap"})

        self.song_1 = Songs("Kings Of Leon", "Charmer", 4)
        self.song_2 = Songs("Arctic Monkeys", "Flourecent Adolescent", 3)
        self.song_3 = Songs("Jay-Z", "Empire State Of Mind", 5)
        self.song_4 = Songs("Chance The Rapper", "Acid Rap", 5)

        self.prefered_playlist_1 = [self.song_1, self.song_2]
        self.group_1 = [self.guest_1, self.guest_2, self.guest_3, self.guest_4]
        self.group_2 = [self.guest_1, self.guest_2, self.guest_3]
        self.group_2_playlist = [self.song_1,
                                 self.song_2, self.song_3, self.song_4]
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
        prefered_playlist = [self.song_1, self.song_2]
        self.room_1.add_songs_to_playlist(prefered_playlist)
        self.assertEqual(2, len(self.room_1.playlist))

    def test_can_remove_song_from_playlist(self):
        prefered_playlist = [self.song_1, self.song_2]
        self.room_1.remove_songs_from_playlist(prefered_playlist, self.song_1)
        self.assertEqual(1, len(self.room_1.playlist))

    def test_add_playlist_to_playlist(self):
        self.room_1.add_songs_to_playlist(self.prefered_playlist_1)
        self.assertEqual(2, len(self.room_1.playlist))

    def test_room_reach_capacity(self):
        self.room_5.add_guest(self.group_1)
        full_room = self.room_5.room_is_full()
        self.assertEqual("the room is now full", full_room)

    def test_begin_a_session(self):
        self.room_1.begin_a_session(
            self.room_1, self.group_2, self.group_2_playlist)
        self.assertEqual(3, self.room_1.num_guests)
        self.assertEqual(4, len(self.room_1.playlist))
        self.assertEqual(3, self.room_1.num_guests)
        self.assertEqual(30, self.room_1.cash)
        self.assertEqual(20, self.guest_1.wallet)

    def test_guest_pay_for_session(self):
        self.room_1.take_payment_for_session(self.room_1, self.group_1)
        self.assertEqual(30, self.room_1.cash)
        self.assertEqual(20, self.guest_1.wallet)
