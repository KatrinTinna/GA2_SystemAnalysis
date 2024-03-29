#!/bin/python3.11
from user import *
import typing


class StudyGroup:
    def __init__(
        self,
        course="",
        name="",
        members: list[User] = [],
        admin: User = "",
        description="",
        max_members=100,
    ):
        self.course = course
        self.name = name
        self.members = members
        self.admin = admin
        self.description = description
        self.max_members = max_members

    @classmethod
    def make_study_group(
        cls, course, name, members, admin, description, max_members=100
    ):
        """Makes sure all the parameters have valid values. If not the function returns False,
        otherwise it makes an instance of a StudyGroup.

        Args:
            course (str): The name of the course.
            name (str): The name of the studygroup.
            members (list[Users]): A list of users that are a part of the studygroup.
            admin (User): The admin of the group.
            description (str): A short description of the group.
            max_members (int): A number representing max number of members in the group.

        Returns:
            bool or Studygroup: False or an istance of the Studygroup class.
        """
        if name == "" or description == "" or course == "":
            print("The studygroup needs to have a valid course, name and description!")
            return False
        elif len(members) > max_members:
            print("There are two many members in this group!")
            return False
        elif type(admin) != User:
            print("The admin is not a valid user!")
            return False
        for user in members:
            if course not in user.courses:
                members.remove(user)
        return cls(course, name, members, admin, description, max_members)

    def add_member(self, member: User):
        """Adds a member to the members list of the study group. Checks if the member
        is valid.

        Args:
            member (User): A member which is a User object.

        Returns:
            None: Returns None.
        """
        if type(member) != User:
            return None
        elif member in self.members:
            return None
        elif len(self.members) == self.max_members:
            return None
        elif self.course not in member.courses:
            return None
        else:
            self.members.append(member)
            return None

    def remove_member(self, member: User):
        """Removes a member from the members list of the study group.

        Args:
            member (User): A member which is a User object.

        Returns:
            None: Returns None.
        """
        if type(member) != User:
            return None
        elif member in self.members:
            self.members.remove(member)
            return None
        else:
            return None
