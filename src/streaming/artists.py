"""
artists.py
----------
Implement the Artist class representing musicians and content creators.

Classes to implement:
  - Artist
"""

class Artist:
    def __init__(self,artist_id,name,genre,tracks):
        self.artist_id = artist_id
        self.name = name
        self.genre = genre
        self.tracks = tracks

    def add_track(self,track):
        pass

    def track_count(self):
        pass