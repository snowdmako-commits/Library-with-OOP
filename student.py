from book import *

class Student:

    def __init__(self, studentID, name):
        self.studentID = studentID
        self.name = name
        self.borrowedBooks = []


    def showInfo(self):

        print(f"""
        ID: {self.studentID}
        Name: {self.name}
        Borrowed books: {len(self.borrowedBooks)}
        """)