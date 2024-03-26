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



if __name__ == "__main__":
    cov = coverage.Coverage()
    cov.start()

    unittest.main()

    cov.stop()
    cov.save()

    cov.html_report()
    print("Done.")

    
