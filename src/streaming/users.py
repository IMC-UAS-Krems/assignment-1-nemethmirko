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
    def __init__(self, user_id: str, name: str, age: int, sessions: list):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.sessions = sessions

    def add_session(self, session):
        pass

    def total_listening_seconds(self):
        pass

    def total_listening_minutes(self):
        pass

    def unique_tracks_listened(self):
        pass


class FreeUser(User):
    def __init__(self, user_id, name, age, sessions, MAX_SKIPS_PER_HOUR=6):
        super().__init__(user_id, name, age, sessions)
        self.MAX_SKIPS_PER_HOUR = MAX_SKIPS_PER_HOUR


class PremiumUser(User):
    def __init__(self, user_id, name, age, sessions, subscription_start: datetime.date):
        super().__init__(user_id, name, age, sessions)
        self.subscription_start = subscription_start


class FamilyAccountUser(User):
    def __init__(self, user_id, name, age, sessions, sub_users: list['FamilyMember']):
        super().__init__(user_id, name, age, sessions)
        self.sub_users = sub_users

    def add_sub_user(self, sub_user):
        pass

    def all_members(self):
        pass


class FamilyMember(User):
    def __init__(self, user_id, name, age, sessions, parent: 'FamilyAccountUser'):
        super().__init__(user_id, name, age, sessions)
        self.parent = parent
