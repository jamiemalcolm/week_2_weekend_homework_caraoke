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
