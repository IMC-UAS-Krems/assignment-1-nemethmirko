"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""
import datetime

from src.streaming.albums import Album
from src.streaming.artists import Artist
from src.streaming.playlists import Playlist
from src.streaming.sessions import ListeningSession
from src.streaming.tracks import Track
from src.streaming.users import User


class StreamingPlatform:
    def __init__(self, name: str):
        self.name = name
        self._catalogue: dict[str, Track] = {}
        self._users: dict[str, User] = {}
        self._artists: dict[str, Artist] = {}
        self._albums: dict[str, Album] = {}
        self._playlists: dict[str, Playlist] = {}
        self._sessions: list[ListeningSession] = []

    def add_track(self, track: Track):
        self._catalogue[track.track_id] = track
        return "Track added to catalogue"

    def add_user(self, user: User):
        self._users[user.user_id] = user
        return "User added to users"

    def add_artist(self, artist: Artist):
        self._artists[artist.artist_id] = artist
        return "Artist added to artists"

    def add_album(self, album: Album):
        self._albums[album.album_id] = album
        return "Album added to albums"

    def add_playlist(self, playlist: Playlist):
        self._playlists[playlist.playlist_id] = playlist
        return "Playlist added to playlists"

    def record_session(self, session: ListeningSession):
        if session.user.user_id in self._users and session.track.track_id in self._catalogue:
            self._sessions.append(session)
            session.user.add_session(session)
        else:
            print("Error: User or Track not found in platform records.")

    def get_track(self, track_id: str):
        # returns the track by the given id
        return self._catalogue.get(track_id)

    def get_user(self, user_id: str):
        # returns a user by the given id
        return self._users.get(user_id)

    def get_artist(self, artist_id: str):
        # returns the artist by the given id
        return self._artists.get(artist_id)

    def get_album(self, album_id: str):
        # returns the album by the given id
        return self._albums.get(album_id)

    def all_users(self) -> list:
        # returns all users
        return list(self._users.values())

    def all_tracks(self) -> list:
        # returns all tracks
        return list(self._catalogue.values())

    def total_listening_time_minutes(self, start: datetime.time, end: datetime.time) -> float:
        pass

    def avg_unique_tracks_per_premium_user(self, days: int = 30) -> float:
        pass

    def track_with_most_distinct_listeners(self):
        pass

    def avg_session_duration_by_user_type(self) -> list[tuple[str, float]]:
        pass

    def total_listening_time_underage_sub_users_minutes(self, age_threshold: int = 18) -> float:
        pass

    def top_artists_by_listening_time(self, n: int = 5):
        pass

    def user_top_genre(self, user_id: str) -> tuple[str, float] | None:
        pass

    def collaborative_playlists_with_many_artists(self, threshold: int = 3):
        pass

    def avg_tracks_per_playlist_type(self) -> dict[str, float]:
        pass

    def users_who_completed_albums(self):
        pass
