#!/bin/python3.11
from user import User
import unittest

class TestPostProblem(unittest.TestCase):
    """"This class will test if the Post problem feature is working correctly."""

    def test_post_problem_friends(self):
        """Tests posting a problem.
        """
        friend1 = User("Anna")
        friend2 = User("Arna")
        friend3 = User("Hera")
        user = User("Katrín", "Student", ["Math"], "katrins",[], [friend1, friend2,friend3], "katrins23@ru.is")
        problem = "How do I make a github repository?"
        result = user.post_problem(problem, "Friends")
        print(result)
        self.assertTrue(result)
        for friend in user.friends:
            self.assertIn(problem, friend.feed)

    
    def test_post_empty_problem(self):
        """Tests posting a empty problem.
        """
        friend1 = User("Anna")
        friend2 = User("Arna")
        friend3 = User("Hera")
        user = User("Katrín", "Student", ["Math"], "katrins",[], [friend1, friend2,friend3], "Katrins@ru.is")
        problem = ""
        result = user.post_problem(problem, "Friends")  
        self.assertFalse(result)
        for friend in user.friends:
            self.assertNotIn(problem, friend.feed)


    def test_post_problem_everyone(self):
        """Tests posting a problem to every user in the system.
        """
        user1 = User("Anna")
        user2 = User("Arna")
        user3 = User("Hera")
        user = User("Katrín", "Student", ["Math"], "katrins",[], [], "Katrins@ru.is")
        problem = "How do I make a sequence diagram?"
        result = user.post_problem(problem)  
        self.assertTrue(result)
        all_user = User.get_all_users()
        print(all_user)
        for user in all_user:
            self.assertIn(problem, user.feed)


    def test_post_problem_no_email(self):
        """Tests trying to post a problem with no email registered.
        """
        user1 = User("Anna")
        user2 = User("Arna")
        user3 = User("Hera")
        user = User("Katrín", "Student", ["Math"], "katrins",[], [user1, user2, user3])
        problem = "How do I learn about the WW2"
        result = user.post_problem(problem)  
        self.assertFalse(result)
        for user in user.friends:
            self.assertNotIn(problem, user.feed)


    def test_post_problem_to_noone(self):
        """Tests trying to post a problem for no one to see.
        """
        user1 = User("Anna")
        user2 = User("Arna")
        user3 = User("Hera")
        user = User("Katrín", "Student", ["Math"], "katrins",[], [user1, user2, user3], "Katrins23@ru.is")
        problem = "How do I make a diagram?"
        result = user.post_problem(problem, "")  
        self.assertFalse(result)
        for user in user.friends:
            self.assertNotIn(problem, user.feed)


        