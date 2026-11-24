from book import Book
from student import Student
from library import Library

library = Library("My Library")

 
library.addBook(Book(1, "Harry Potter", "J.K. Rowling", 350))
library.addBook(Book(2, "The Hobbit", "J.R.R. Tolkien", 295))
library.addBook(Book(3, "1984", "George Orwell", 328))
library.addBook(Book(4, "The Little Prince", "Antoine de Saint-Exupery", 96))
library.addBook(Book(5, "Clean Code", "Robert Martin", 464))
 
library.addStudent(Student(1, "Ali"))
library.addStudent(Student(2, "Ahmed"))
library.addStudent(Student(3, "Murad"))
library.addStudent(Student(4, "Leyla"))
library.addStudent(Student(5, "Aysel"))

while True:
    print("""
========== LIBRARY SYSTEM ==========

1. Add Book
2. Add Student
3. Show Books
4. Show Students
5. Borrow Book
6. Return Book
7. Exit

====================================
""")

    choice = input("Enter your choice: ")