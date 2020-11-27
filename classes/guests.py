class Guests():

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def can_afford_session(self, room):
        if self.wallet >= room.price:
            return True
        return False

    def pay_for_session(self, room):
        self.wallet -= room.price
