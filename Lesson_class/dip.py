from enum import Enum
from abc import ABC, abstractmethod

class Teams(Enum):
    BLUE_TEAM = 1
    RED_TEAM = 2
    GREEN_TEAM = 3

class TeamMembershipLookUP:
    @abstractmethod
    def find_all_student(self, team):
        pass

class Student:
    def __init__(self, name) -> None:
        self.name = name

class TeamMemberShips(TeamMembershipLookUP):
    def __init__(self) -> None:
        self.team_membership = []

    def add_team_member(self, student, team):
        self.team_membership.append((student, team))

    def find_all_student(self, team):
        for members in self.team_membership:
            if members[1] == team:
                yield members[0].name

class Analysis:
    def __init__(self, team_membership_lookup) -> None:
        for student in team_membership_lookup.find_all_student(Teams.RED_TEAM):
            print(f"{student} is in RED team")

student1 = Student("Oleg")
student2 = Student("Biba")
student3 = Student("Boba")

team_membership = TeamMemberShips()
team_membership.add_team_member(student1, Teams.RED_TEAM)
team_membership.add_team_member(student2, Teams.RED_TEAM)
team_membership.add_team_member(student3, Teams.BLUE_TEAM)

Analysis(team_membership)