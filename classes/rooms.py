class Rooms():

    def __init__(self, name, time_limit, price, capacity):
        self.name = name
        self.time_limit = time_limit
        self.price = price
        self.capacity = capacity
        self.playlist = []
        self.cash = 0
        self.num_guests = 0
