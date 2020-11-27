class Rooms():

    def __init__(self, name, time_limit, price, capacity):
        self.name = name
        self.time_limit = time_limit
        self.price = price
        self.capacity = capacity
        self.playlist = []
        self.cash = 0
        self.num_guests = 0

    def add_guest(self):
        self.num_guests += 1

    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def remove_song_from_playlist(self, played_song):
        for song in self.playlist:
            if song == played_song:
                self.playlist.remove(song)
