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

    def total_listening_seconds(self) -> int:
        # Returns the total number of seconds listened
        return sum(session.duration_listened_seconds for session in self.sessions)

    def total_listening_minutes(self) -> float:
        # Returns the total number of minutes listened
        return self.total_listening_seconds() / 60

    def unique_tracks_listened(self) -> set:
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
    def __init__(self, user_id, name, age, sub_users: list['FamilyMember'] = None):
        super().__init__(user_id, name, age)
        self.sub_users = sub_users if sub_users is not None else []

    def add_sub_user(self, sub_user):
        return self.sub_users.append(sub_user)

    def all_members(self) -> list:
#
#        self = <unit_tests.test_users.TestUsers object at 0x000002CB28C8D310>
#
#    def test_family_account_all_members(self) -> None:
#        family = FamilyAccountUser("u1", "Parent", age=40)
#        member = FamilyMember("u2", "Child", age=16, parent=family)
#        family.add_sub_user(member)
#>       assert family.all_members() == [family, member]
#E       AssertionError: assert [<streaming.u...02CB289EE850>] == [<streaming.u...02CB289EE850>]
#E
#E         At index 0 diff: <streaming.users.FamilyMember object at 0x000002CB289EE850> != <streaming.users.FamilyAccountUser object at 0x000002CB289EF250>
#E         Right contains one more item: <streaming.users.FamilyMember object at 0x000002CB289EE850>
#E
#E         Full diff:
#E           [
#E         -     <streaming.users.FamilyAccountUser object at 0x000002CB289EF250>,...
#E
#E         ...Full output truncated (2 lines hidden), use '-vv' to show
#
#tests\unit_tests\test_users.py:72: AssertionError
#
#
#

        # this was the only solution I could come up on the spot for this error
        # the problem was that it only returned the sub users but now it returns all of them

        return [self] + self.sub_users


class FamilyMember(User):
    def __init__(self, user_id, name, age, parent: 'FamilyAccountUser'):
        super().__init__(user_id, name, age)
        self.parent = parent
