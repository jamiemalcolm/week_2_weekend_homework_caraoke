import unittest

from classes.guests import Guests
from classes.rooms import Rooms
from classes.songs import Songs


class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guests("Ann", 50, 45)
        self.guest_2 = Guests("Bill", 40, 35)
        self.guest_3 = Guests("Carl", 30, 22)
        self.guest_4 = Guests("Dee", 15, 18)