"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""
import datetime
from itertools import dropwhile

from src.streaming.albums import Album
from src.streaming.artists import Artist
from src.streaming.playlists import Playlist, CollaborativePlaylist
from src.streaming.sessions import ListeningSession
from src.streaming.tracks import Track, Song
from src.streaming.users import User, PremiumUser, FamilyAccountUser


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
        total_seconds = 0

        for session in self._sessions:
            session_time_only = session.timestamp.time()
            if start <= session_time_only <= end:
                total_seconds += session.duration_listened_seconds
        return float(total_seconds / 60)

    def avg_unique_tracks_per_premium_user(self, days: int = 30) -> float:
        # gets all premium users and their unique tracks listened attribute and sums is up and divides it by the number of premium users
        premium_users = [u for u in self._users.values() if isinstance(u, PremiumUser)]

        if not premium_users:
            return 0.0

        days_limit = datetime.datetime.now() - datetime.timedelta(days)

        total_unique_count = 0

        for user in premium_users:
            # gets unique tracks of the last 30 days
            recent_tracks = set()
            for session in user.sessions:
                if session.timestamp >= days_limit:
                    recent_tracks.add(session.track.track_id)

            total_unique_count += len(recent_tracks)

        return float(total_unique_count / len(premium_users))

    def track_with_most_distinct_listeners(self) -> Track | None:
        # dict to store unique listeners and tracks by user id and track id
        t_listeners = {}
        if not self._sessions:
            return None

        for session in self._sessions:
            t_id = session.track.track_id
            u_id = session.user.user_id

            # set so it is unique
            if t_id not in t_listeners:
                t_listeners[t_id] = set()

            t_listeners[t_id].add(u_id)
        # empty return none
        if not t_listeners:
            return None
        # by filtering the dict we look for most listened track with max and a lambda statement (where the lenght of track id-s is the biggest)
        most_listened_track = max(t_listeners, key=lambda tid: len(t_listeners[tid]))

        return self.get_track(most_listened_track)

    def avg_session_duration_by_user_type(self) -> list[tuple[str, float]]:
        if not self._sessions:
            return []

        t_durations = {}

        for session in self._sessions:
            # using __name__ to get the class name as a string
            u_type = type(session.user).__name__
            duration = session.duration_listened_minutes() * 60

            if u_type not in t_durations:
                t_durations[u_type] = []

            t_durations[u_type].append(duration)
        # list of average session durations
        averages = []
        for u_types, durations in t_durations.items():
            avg = sum(durations) / len(durations)
            averages.append((u_types, float(avg)))
        # sorted in descending order
        return sorted(averages, key=lambda x: x[1], reverse=True)

    def total_listening_time_underage_sub_users_minutes(self, age_threshold: int = 18) -> float:
        total_time = 0
        for user in self._users.values():
            # checks for sub users as per the requirements
            if isinstance(user, FamilyAccountUser):
                for sub_user in user.sub_users:
                    if sub_user.age < age_threshold:
                        # sums up the listening minutes with the already integrated function in users
                        total_time += sub_user.total_listening_minutes()

        return float(total_time)

    def top_artists_by_listening_time(self, n: int = 5) -> list[tuple[Artist, float]]:
        if not self._sessions:
            return []

        artist_listening_times = {}

        for session in self._sessions:
            track = session.track
            # check if it has the attribute artists because podcasts don't have it
            if isinstance(track, Song):
                artist = track.artist
                duration = session.duration_listened_minutes()
                artist_listening_times[artist] = artist_listening_times.get(artist, 0) + duration
        # convert to list of tuples
        artist_lists = list(artist_listening_times.items())
        # sort by descending to get top
        artist_lists.sort(key=lambda x: x[1], reverse=True)
        # return top 5 of the list
        return artist_lists[:n]

    def user_top_genre(self, user_id: str) -> tuple[str, float] | None:
        user = self.get_user(user_id)
        if not user or not user.sessions:
            return None

        genres_listened_to = {}
        total_time = 0
        for session in user.sessions:
            genre = session.track.genre
            duration = session.duration_listened_minutes()

            # summing the time and put it into the dict
            genres_listened_to[genre] = genres_listened_to.get(genre, 0) + duration
            total_time += duration

        if not genres_listened_to:
            return None

            # getting the most listened to gerne
        top_genre = max(genres_listened_to, key=genres_listened_to.get)
        percentage = (genres_listened_to[top_genre] / total_time) * 100
        return (top_genre, float(percentage))

    def collaborative_playlists_with_many_artists(self, threshold: int = 3) -> list:
        collaborative_playlists = []
        for playlist in self._playlists.values():
            # checking if playlist is a collaborative playlist
            if isinstance(playlist, CollaborativePlaylist):
                # collect all artist id-s into a set so they are unique
                unique_artists = set()
                for track in playlist.tracks:
                    if isinstance(track, Song):
                        unique_artists.add(track.artist.artist_id)

                if len(unique_artists) > threshold:
                    collaborative_playlists.append(playlist)

        return collaborative_playlists

    def avg_tracks_per_playlist_type(self) -> dict[str, float]:
        counts = {"Playlist": [], "CollaborativePlaylist": []}
        for playlist in self._playlists.values():
            # because of __name__ we get specifically Playlist or CollaborativePlaylist as return
            p_type = type(playlist).__name__
            if p_type in counts:
                counts[p_type].append(len(playlist.tracks))
        # calculate averages (thedefault is 0)
        averages = {"Playlist": 0.0, "CollaborativePlaylist": 0.0}
        for p_type, track_counts in counts.items():
            if track_counts:
                averages[p_type] = float(sum(track_counts) / len(track_counts))

        return averages

    def users_who_completed_albums(self):
        listened_to_every_track = []
        for user in self._users.values():
            listened_track_ids = user.unique_tracks_listened()
            completed_alum_titles = []

            for album in self._albums.values():
                required_ids = album.track_ids()
                # if album has no tracks we contniue ansd it is ignored
                if len(required_ids) == 0:
                    continue
                # checks if every item of required ids is an item in listened track ids
                if required_ids.issubset(listened_track_ids):
                    completed_alum_titles.append(album.title)
            # if completed at least one add to list
            if completed_alum_titles:
                listened_to_every_track.append((user, completed_alum_titles))

        return listened_to_every_track
