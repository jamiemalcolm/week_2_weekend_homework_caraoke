from classes.guests import Guests
from classes.songs import Songs


class Rooms():

    def __init__(self, name, time_limit, price, capacity):
        self.name = name
        self.time_limit = time_limit
        self.price = price
        self.capacity = capacity
        self.playlist = []
        self.cash = 0
        self.num_guests = 0

    def add_guest(self, group):
        self.num_guests += len(group)

    def add_songs_to_playlist(self, song):
        self.playlist = song

    def remove_songs_from_playlist(self, prefered_music, played_song):
        self.playlist = prefered_music
        for song in self.playlist:
            if song == played_song:
                self.playlist.remove(song)

    def room_is_full(self):
        if self.num_guests == self.capacity:
            return "the room is now full"

    def begin_a_session(self, room, group, playlist):
        self.add_guest(group)
        self.add_songs_to_playlist(playlist)
        self.take_payment_for_session(room, group)

    def take_payment_for_session(self, room, group):
        group[0].wallet -= self.price
        self.cash += self.price
