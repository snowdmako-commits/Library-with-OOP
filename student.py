from book import *

class Student:

    def __init__(self, studentID, name):
        self.studentID = studentID
        self.name = name
        self.borrowedBooks = []