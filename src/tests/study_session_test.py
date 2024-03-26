#!/bin/python3.11

from user import User

from study_session import StudySession
import unittest
import datetime
import coverage

class TestAdvertisingStudySession(unittest.TestCase):
    """This class will test if the Advertise Study Session feature is working correctly."""

    def test_advertise_studysession(self):
        """Tests advertising a studysession"""
        TA = User("Anna", "TA")
        study_session = StudySession("Math", "We will cover linear algebra", datetime.datetime(24,3,27), datetime.time(12), 1, TA, 1, 4000)
        expected_result = "Advertised"
        study_session.advertise_studysession()
        #Let´s assume that if the studysession is advertised successfully, then the advertise_status attribute will change.
        self.assertEqual(expected_result, study_session.advertise_status)

    def test_advertise_studysession_invalid_subject(self):
        """Tests trying to advertise a studysession with an invalid subject."""
        TA = User("Siggi", "TA")
        study_session = StudySession(1, "We will look at data strctures", datetime.datetime(24,5,23), datetime.time(13),2,TA,3, 5000)
        expected_result = "Unadvertised"
        #Let´s assume that if the studysession is advertised successfully, then the advertise_status attribute will change.
        self.assertEqual(expected_result, study_session.advertise_status)


    def test_advertise_studysession_invalid_description(self):
        """Tests trying to advertise a studysession with an invalid description."""
        TA = User("Steinunn", "TA")
        study_session = StudySession("Math", 2, datetime.datetime(24,5,11), datetime.time(10), 2, TA, 3, 2000)
        expected_result = "Unadvertised"
        #Let´s assume that if the studysession is advertised successfully, then the advertise_status attribute will change.
        self.assertEqual(expected_result, study_session.advertise_status)


    def test_advertise_studysession_invalid_date(self):
        """Tests trying to advertise a studysession with an invalid date."""
        TA = User("Guðmundur", "TA")
        study_session = StudySession("Math", "We will look at discrete math", "x", datetime.time(12), 2, TA, 3, 3000)
        expected_result = "Unadvertised"
        #Let´s assume that if the studysession is advertised successfully, then the advertise_status attribute will change.
        self.assertEqual(expected_result, study_session.advertise_status)
    
    def test_advertise_studysession_invalid_time(self):
        """Tests trying to advertise a studysession with an invalid time."""
        TA = User("Ari", "TA")
        study_session = StudySession("Programming", "We will look at Python",datetime.datetime(24,5,12), datetime.time(17),1, TA, 1, 7500 )
        expected_result = "Unadvertised"
        #Let´s assume that if the studysession is advertised successfully, then the advertise_status attribute will change.
        self.assertEqual(expected_result, study_session.advertise_status)

    
    def test_advertise_studysession_invalid_maxstudents(self):
        """Tests trying to advertise a studysession with an invalid number of max students"""
        TA = User("Katrín", "TA")
        study_session = StudySession("History", "We will look at WW2", datetime.datetime(24,5,16), datetime.time(15), 4,TA,0, 3000)
        expected_result = "Unadvertised"
        #Let´s assume that if the studysession is advertised successfully, then the advertise_status attribute will change.
        self.assertEqual(expected_result, study_session.advertise_status)

    
    def test_advertise_studysession_invalid_instructor(self):
        """Tests trying to advertise a studysession with an invalid instructor"""
        TA = User("Katrín")
        study_session = StudySession("Math", "We will look at imaginary numbers", datetime.datetime(24,4,12), datetime.time(12),2, TA, 3,2000)
        expected_result = "Unadvertised"
        #Let´s assume that if the studysession is advertised successfully, then the advertise_status attribute will change.
        self.assertEqual(expected_result, study_session.advertise_status)
    

    def test_advertise_studysession_invalid_duration(self):
        """Tests trying to advertise a studysession with an invalid duration"""
        TA = User("Katrín", "TA")
        study_session = StudySession("Math", "Calculus", datetime.datetime(24,2,3), datetime.time(11),"x", TA, 2, 2000)
        expected_result = "Unadvertised"
        #Let´s assume that if the studysession is advertised successfully, then the advertise_status attribute will change.
        self.assertEqual(expected_result, study_session.advertise_status)
    

    def test_advertise_studysession_to_many_students(self):
        """Tests trying to advertise a studysession with to many students already signed up"""
        user1 = User("Anna")
        user2 = User("Arna")
        user3 = User("Hera")
        user4 = User("Katrín")
        user5 = User("Bjarki")
        user6 = User("Smári")
        TA = User("Harpa", TA)
        students = [user1, user2,user3,user4,user5,user6]
        study_session = StudySession("Math", "Linear algebra", datetime.datetime(23,2,13), datetime.time(14), 2,TA,4,2000, students)
        expected_result = "Unadvertised"
        #Let´s assume that if the studysession is advertised successfully, then the advertise_status attribute will change.
        self.assertEqual(expected_result, study_session.advertise_status)
    

    def test_advertise_studysession_invalid_price(self):
        """Tests trying to advertise a studysession with an invalid price."""
        TA = User("Katrín", "TA")
        study_session = StudySession("Math", "Algebra", datetime.datetime(24,3,3), datetime.time(12), 2, TA, 2, -1000)
        expected_result = "Unadvertised"
        #Let´s assume that if the studysession is advertised successfully, then the advertise_status attribute will change.
        self.assertEqual(expected_result, study_session.advertise_status)




if __name__ == "__main__":
    cov = coverage.Coverage()
    cov.start()

    unittest.main()

    cov.stop()
    cov.save()

    cov.html_report()
    print("Done.")