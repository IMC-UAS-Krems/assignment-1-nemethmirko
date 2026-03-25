"""
playlists.py
------------
Implement playlist classes for organizing tracks.

Classes to implement:
  - Playlist
    - CollaborativePlaylist
"""

class Playlist:
    def __init__(self,playlist_id:str,name:str,owner,tracks:list):
        self.playlist_id = playlist_id
        self.name = name
        self.owner = owner
        self.tracks = tracks

    def add_track(self,track):
        return self.tracks.append(track)

    def remove_track(self,track_id):
        return self.tracks.remove(track_id) #not sure

    def total_duration_seconds(self):
        pass


class CollaborativePlaylist(Playlist):
    def __init__(self,playlist_id,name,owner,tracks,contributors:list):
        super().__init__(playlist_id,name,owner,tracks)
        self.contributors = contributors

    def add_contributor(self,user):
        return self.contributors.append(user)

    def remove_contributor(self,user):
        return self.contributors.remove(user) #not sure