class User:
    def __init__(self, name = "", username = "", id = 0, password = "", role = "Student"):
        self.name = name
        self.username = username
        self.id = id
        self.__password = password
        self.role = role



