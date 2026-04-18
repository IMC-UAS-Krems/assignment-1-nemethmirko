"""
artists.py
----------
Implement the Artist class representing musicians and content creators.

Classes to implement:
  - Artist
"""


class Artist:
    def __init__(self, artist_id: str, name: str, genre: str):
        self.artist_id = artist_id
        self.name = name
        self.genre = genre
        self.tracks: list = []

    def add_track(self, track):
        return self.tracks.append(track)

    def track_count(self) ->int:
        #Counts all tracks
        return len(self.tracks)
