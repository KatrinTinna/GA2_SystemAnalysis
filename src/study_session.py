#!/bin/python3.11

import typing
from datetime import *
from user import *

class StudySession:
    def __init__(self, subject = "",description = "",date = "", time = 0, duration = 1, TA : User = "", max_students = 1,price = 0, students : list[User] = [], status = "On schedule", advertise_status = "Unadvertised",location = "Reykjavik"):
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


    def advertise_studysession(self):
        """Makes sure that all the attributes of the studysession instance
        are valid and that the studysession is qualified to be advertised. Returns nothing.
        """
        if self.status != "On schedule":
            print("The study session needs to be on schedule to advertise it.")
        if type(self.max_students) != int and (1 <= self.max_students <= 8):
            print("The number of max students is invalid.")
        if self.subject.isnumeric() or self.description.isnumeric():
            print("The subject and description of the studysession needs to be valid!")
        if self.advertise_status == "Advertised":
            print("This study session has already been advertised.")
        if self.TA.role != "TA":
            print("The instructor for the studysession needs to be a TA!")
        elif type(self.date) != datetime and type(self.time) != datetime:
            print("The date and time need to be valid!")
        elif type(self.duration) == str:
            print("The duration should be a number!")
        elif len(self.students) > self.max_students:
            print("There are to many students already signed up for the study session!")
        elif type(self.price) != int and (self.price < 0):
            print("The price is not valid!")
        else:
            self.advertise_status = "Advertised"
            print(f"""
            {self.subject}
            {self.description}
            When :{self.date}, {self.time}
            Where : {self.location}
            Spots available : {self.max_students - len(self.students)}
            TA : {self.TA}
            Email me to join! {self.TA.email}""")


    
        

    
    
        
        

    

