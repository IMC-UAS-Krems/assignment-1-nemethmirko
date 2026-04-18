"""
users.py
--------
Implement the class hierarchy for platform users.

Classes to implement:
  - User (base class)
    - FreeUser
    - PremiumUser
    - FamilyAccountUser
    - FamilyMember
"""

import datetime


class User:
    def __init__(self, user_id: str, name: str, age: int):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.sessions = []

    def add_session(self, session):
        return self.sessions.append(session)

    def total_listening_seconds(self)->int:
        #Returns the total number of seconds listened
        return sum(session.duration_listened_seconds for session in self.sessions)

    def total_listening_minutes(self)->float:
        #Returns the total number of minutes listened
        return self.total_listening_seconds()/60

    def unique_tracks_listened(self)->set:
        return {session.track.track_id for session in self.sessions}


class FreeUser(User):
    def __init__(self, user_id, name, age, MAX_SKIPS_PER_HOUR=6):
        super().__init__(user_id, name, age)
        self.MAX_SKIPS_PER_HOUR = MAX_SKIPS_PER_HOUR


class PremiumUser(User):
    def __init__(self, user_id, name, age, subscription_start: datetime.date):
        super().__init__(user_id, name, age)
        self.subscription_start = subscription_start


class FamilyAccountUser(User):
    def __init__(self, user_id, name, age, sub_users: list['FamilyMember']):
        super().__init__(user_id, name, age)
        self.sub_users = sub_users

    def add_sub_user(self, sub_user):
        return self.sub_users.append(sub_user)

    def all_members(self)->list:
        return self.sub_users


class FamilyMember(User):
    def __init__(self, user_id, name, age, parent: 'FamilyAccountUser'):
        super().__init__(user_id, name, age)
        self.parent = parent
