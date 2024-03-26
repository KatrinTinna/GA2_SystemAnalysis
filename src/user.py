

class User:
    def __init__(self, name = "", role = "Student", courses = [],username = "", id = 0, password = "", email = ""):
        self.name = name
        self.username = username
        self.id = id
        self.__password = password
        self.role = role
        self.courses = courses
        self.email = email



