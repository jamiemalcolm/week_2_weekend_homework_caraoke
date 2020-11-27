import unittest

from classes.guests import Guests
from classes.rooms import Rooms
from classes.songs import Songs


class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guests("Ann", 50, 45)
        self.guest_2 = Guests("Bill", 40, 35)
        self.guest_3 = Guests("Carl", 30, 18)
        self.guest_4 = Guests("Dee", 5, 17)

        self.room_1 = Rooms("Red", 60, 30, 25)
        self.room_2 = Rooms("Yellow", 30, 15, 10)
        self.room_3 = Rooms("Green", 45, 20, 15)
        self.room_4 = Rooms("Blue", 60, 25, 10)
        self.room_5 = Rooms("Orange", 10, 5, 4)

        group_1 = [self.guest_1]
# basic test assuring class set up correctly

    def test_guest_has_name(self):
        self.assertEqual("Ann", self.guest_1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(40, self.guest_2.wallet)

    def test_guest_has_age(self):
        self.assertEqual(17, self.guest_4.age)

    def test_can_afford_session__true(self):
        can_afford = self.guest_1.can_afford_session(self.room_2)
        self.assertEqual(True, can_afford)

    def test_can_afford_session__flase(self):
        can_afford = self.guest_4.can_afford_session(self.room_1)
        self.assertEqual(False, can_afford)

    def test_can_pay_for_session(self):
        self.guest_1.pay_for_session(self.room_1)
        self.assertEqual(20, self.guest_1.wallet)
