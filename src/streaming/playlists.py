"""
playlists.py
------------
Implement playlist classes for organizing tracks.

Classes to implement:
  - Playlist
    - CollaborativePlaylist
"""


class Playlist:
    def __init__(self, playlist_id: str, name: str, owner):
        self.playlist_id = playlist_id
        self.name = name
        self.owner = owner
        self.tracks = []

    def add_track(self, track):
        return self.tracks.append(track)

    def remove_track(self, track_id):
        # Filters out the track we do not need by the ID provided
        self.tracks = [track for track in self.tracks if track.track_id != track_id]
        return "Track removed from tracks"

    def total_duration_seconds(self) -> int:
        return sum(track.duration_seconds for track in self.tracks)


class CollaborativePlaylist(Playlist):
    def __init__(self, playlist_id, name, owner, contributors=None):
        super().__init__(playlist_id, name, owner)
        self.contributors = contributors if contributors is not None else[owner]

    def add_contributor(self, user):
        return self.contributors.append(user)

    def remove_contributor(self, user):
        self.contributors = [c for c in self.contributors if c.user != user]
        return "User removed from contributors"
