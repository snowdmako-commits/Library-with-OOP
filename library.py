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


    def showBooks(self):

        if not self.books:
            print("There are no books.")
            return

        for book in self.books:
            book.showInfo()
            print("----------------------")


    def showStudents(self):

        if not self.students:
            print("There are no students.")
            return

        for student in self.students:
            student.showInfo()
            print("----------------------")


    def searchBook(self, bookID):

        for book in self.books:
            if book.bookID == bookID:
                return book
        return None


    def searchStudent(self, studentID):

        for student in self.students:
            if student.studentID == studentID:
                return student
        return None