"""
albums.py
---------
Implement the Album class for collections of AlbumTrack objects.

Classes to implement:
  - Album
"""

class Album:
    def __init__(self,album,title,artist,release_year,tracks):
        self.album = album
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.tracks = tracks

    def add_track(self,track):
        pass

    def track_ids(self):
        pass

    def duration_seconds(self):
        pass