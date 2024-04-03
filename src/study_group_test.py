#!/bin/python3.11

import unittest
import coverage
from study_group import StudyGroup
from user import User



class TestStudyGroup(unittest.TestCase):
    """This class will test if the Advertise Study Session feature is working correctly."""
    
    def test_make_study_group(self):
        """Tests making a study group
        """
        admin = User("Anna")
        result = StudyGroup.make_study_group("System analysis", "System analysis at RU", [], admin, "In this group we will help each other out", 100 )
        self.assertEqual(type(result), StudyGroup)


    def test_no_name(self):
        """Tests making a study group with no name.
        """
        admin = User("Anna")
        result = StudyGroup.make_study_group("System analysis", "", [], admin, "In this group we will help each other out", 100 )
        self.assertFalse(result)

    def test_no_course(self):
        """Tests making a study group without emphasizing what the course is.
        """
        admin = User("Anna")
        result = StudyGroup.make_study_group("", "System analysis at RU", [], admin, "In this group we will help each other out", 100 )
        self.assertFalse(result)

    def test_invalid_admin(self):
        """Tests making a study group with an invalid admin.
        """
        admin = ""
        result = StudyGroup.make_study_group("System Analysis", "System analysis at RU", [], admin, "In this group we will help each other out", 100 )
        self.assertFalse(result)

    def test_add_member(self):
        """Tests adding a member to a study group.
        """
        member = User("Katrín", "Student", "Math")
        TA = User("Anna", "TA")
        study_group = StudyGroup.make_study_group("Math", "Linear algebra", [], TA, "for linear algebra in RU")
        study_group.add_member(member)
        self.assertIn(member, study_group.members)
    
    def test_add_member_group_full(self):
        """Tests adding a member when the study group is full.
        """
        member = User("Katrín", "Student", "Math")
        TA = User("Anna", "TA")
        study_group = StudyGroup.make_study_group("Math", "Linear algebra", [User("Ragna","Student", "Math" )], TA, "for linear algebra in RU", 1)
        study_group.add_member(member)
        self.assertNotIn(member, study_group.members)
    
    def test_add_member_not_in_course(self):
        """Tests adding a member who is not in the a course.
        """
        member = User("Katrín", "Student", "History")
        TA = User("Anna", "TA")
        study_group = StudyGroup.make_study_group("Math", "Linear algebra", [], TA, "for linear algebra in RU")
        study_group.add_member(member)
        self.assertNotIn(member, study_group.members)

    
    def test_add_member_not_member(self):
        """Tests trying to add a member which is
        not an instance of the User class.
        """
        member = "Elísabet"
        TA = User("Anna", "TA")
        study_group = StudyGroup.make_study_group("Math", "Linear algebra", [], TA, "for linear algebra in RU")
        study_group.add_member(member)
        self.assertNotIn(member, study_group.members)


    def test_add_member_already_in_group(self):
        """Tests trying to add a member which is already in the study group.
        """
        member = User("Katrín", "Student", "History")
        TA = User("Anna", "TA")
        study_group = StudyGroup.make_study_group("Math", "Linear algebra", [member], TA, "for linear algebra in RU")
        study_group.add_member(member)
        self.assertNotIn(member, study_group.members)

    
    def test_removing_a_member(self):
        """Tests removing a member from a study group.
        """
        member = User("Katrín", "Student", "Math")
        TA = User("Hera", "TA")
        study_group = StudyGroup.make_study_group("Math", "Linear algebra", [member], TA, "for linear algebra in RU")
        study_group.remove_member(member)
        self.assertNotIn(member, study_group.members)

    def test_removing_a_member_not_valid(self):
        """Tests removing a member which is not an instance of the User class.
        """
        member = ""
        TA = User("Hera", "TA")
        study_group = StudyGroup.make_study_group("Math", "Linear algebra", [], TA, "for linear algebra in RU")
        study_group.remove_member(member)
        self.assertNotIn(member, study_group.members)

    def test_removing_a_member_empty_group(self):
        """Tests removing a member which has not members.
        """
        member = User("Katrín", "Student", "Math")
        TA = User("Hera", "TA")
        study_group = StudyGroup.make_study_group("Math", "Linear algebra", [], TA, "for linear algebra in RU")
        study_group.remove_member(member)
        self.assertNotIn(member, study_group.members)
        

    def test_removing_a_member_not_in_group(self):
        """Tests removing a member which is not in the group.
        """
        member = User("Katrín", "Student", "Math")
        TA = User("Hera", "TA")
        study_group = StudyGroup.make_study_group("Math", "Linear algebra", [User("Anna", "Student", "Math")], TA, "for linear algebra in RU")
        study_group.remove_member(member)
        self.assertNotIn(member, study_group.members)



if __name__ == "__main__":
    cov = coverage.Coverage()
    cov.start()

    unittest.main()

    cov.stop()
    cov.save()

    cov.html_report()
    print("Done.")

    
