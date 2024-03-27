#!/bin/python3.11

class User:
    all_users = []
    def __init__(self, name = "", role = "Student", courses = [],username = "",feed = [], friends = [], email = "",id = 0, password = ""):
        self.name = name
        self.username = username
        self.id = id
        self.__password = password
        self.role = role
        self.courses = courses
        self.email = email
        self.feed = feed
        self.friends = friends
        User.all_users.append(self)
    

    @classmethod
    def get_all_users(cls):
        return cls.all_users


    def post_problem(self, problem : str, visible_to = "Everyone"):
        """Posts a problem to users feed.

        Args:
            problem (str): A string which reprents the study problem.
            visible_to (str, optional): A string representing who the 
            problem is visible to, either everyone or just the users friends.. Defaults to "Everyone".

        Returns:
            bool: Returns True if the problem was successfully posted, else returns False.
        """
        if problem == "":
            return False
        elif visible_to != "Everyone" or visible_to != "Friends":
            return False
        elif self.email == "":
            return False
        
        else:
            post = f"""
            Posted by {self.username}
            Problem : {problem}
            If you have the answer, please contact me at {self.email}"""
            if visible_to == "Everyone":
                everyone = User.get_all_users()
                for user in everyone:
                    user.feed.append(problem)
                print(post)
                return True
            else:
                for friend in self.friends:
                    friend.feed.append(problem)
                print(post)
                return True





