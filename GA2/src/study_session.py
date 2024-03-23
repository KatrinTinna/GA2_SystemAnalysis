import typing
from datetime import *
from user import *
class StudySessions:
    def __init__(self, subject = "",description = "",date = "", time = 0, duration = 1, TA : User = "", max_students = 1, students : list[User] = [], location = "Reykjavik", status = "On schedule", advertise_status = "Unadvertised", price = 0):
        self.subject = subject
        self.description = description
        self.date = date
        self.time = time
        self.duration = duration
        self.TA = TA
        self.students = students
        self.location = location
        self.advertise_status = advertise_status
        self.status = status
        self.max_students = max_students
        self.price = price


    def advertise_studysession(self, subject,description ,TA, date, time, duration, status, max_students, students, price):
        if status != "On schedule":
            print("The study session needs to be on schedule to advertise it.")
        if type(max_students) != int and (1 <= max_students <= 8):
            print("The number of max students is invalid.")
        if subject.isnumeric() or description.isnumeric():
            print("The subject and description of the studysession needs to be valid!")
        if self.advertise_status == "Advertised":
            print("This study session has already been advertised.")
        if TA.role != "TA":
            print("The instructor for the studysession needs to be a TA!")
        elif type(date) != datetime and type(time) != datetime:
            print("The date and time need to be valid!")
        elif duration.isalpha() == True:
            print("The duration should be a number!")
        elif len(students) > max_students:
            print("There are to many students already signed up for the study session!")
        elif type(price) != int and (price < 0):
            print("The price is not valid!")
        else:
            self.advertise_status = "Advertised"


    
        

    
    
        
        

    

