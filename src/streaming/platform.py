"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""
from src.streaming.albums import Album
from src.streaming.artists import Artist
from src.streaming.playlists import Playlist
from src.streaming.sessions import ListeningSession
from src.streaming.users import User

class StreamingPlatform:
    def __init__(self,name:str,catalogue:dict[str,'Track'],users:dict[str,User],artists:dict[str,Artist],albums:dict[str,Album],playlists:dict[str,Playlist],sessions:list[ListeningSession]):
        self.name = name
        self.catalogue = catalogue
        self.users = users
        self.artists = artists
        self.albums = albums
        self.playlists = playlists
        self.sessions = sessions

    def add_track(self,track):
        pass

    def add_user(self,user):
        pass

    def add_artist(self,artist):
        pass

    def add_album(self,album):
        pass

    def add_playlist(self,playlist):
        pass

    def record_session(self,session):
        pass

    def get_track(self,track_id):
        pass

    def get_user(self,user_id):
        pass

    def get_artist(self,artist_id):
        pass

    def get_album(self,album_id):
        pass

    def all_users(self):
        pass

    def all_tracks(self):
        pass