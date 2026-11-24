from student import *


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.students = []

    def addBook(self, book):
        self.books.append(book)


    def addStudent(self, student):
        self.students.append(student)