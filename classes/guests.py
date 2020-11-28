class Guests():

    def __init__(self, name, wallet, age, favourite_song):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.favourite_song = favourite_song

    def can_afford_session(self, room):
        if self.wallet >= room.price:
            return True
        return False

    def pay_for_session(self, room):
        self.wallet -= room.price
        room.cash += room.price
