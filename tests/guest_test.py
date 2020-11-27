import unittest

from classes.guests import Guests
from classes.rooms import Rooms
from classes.songs import Songs


class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guests("Ann", 50, 45)
        self.guest_2 = Guests("Bill", 40, 35)
        self.guest_3 = Guests("Carl", 30, 18)
        self.guest_4 = Guests("Dee", 15, 17)
# basic test assuring class set up correctly

    def test_guest_has_name(self):
        self.assertEqual("Ann", self.guest_1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(40, self.guest_2.wallet)

    def test_guest_has_age(self):
        self.assertEqual(17, self.guest_4.age)
