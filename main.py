from book import Book
from student import Student
from library import Library

library = Library("My Library")

library.addBook(Book(1, "Harry Potter", "J.K. Rowling", 350))
library.addBook(Book(2, "The Hobbit", "J.R.R. Tolkien", 295))
library.addBook(Book(3, "1984", "George Orwell", 328))
library.addBook(Book(4, "The Little Prince", "Antoine de Saint-Exupery", 96))
library.addBook(Book(5, "Clean Code", "Robert Martin", 464))
library.addBook(Book(6, "To Kill a Mockingbird", "Harper Lee", 281))
library.addBook(Book(7, "The Great Gatsby", "F. Scott Fitzgerald", 180))
library.addBook(Book(8, "Animal Farm", "George Orwell", 112))
library.addBook(Book(9, "Pride and Prejudice", "Jane Austen", 432))
library.addBook(Book(10, "The Alchemist", "Paulo Coelho", 208))
library.addBook(Book(11, "Dune", "Frank Herbert", 412))
library.addBook(Book(12, "Dracula", "Bram Stoker", 418))
library.addBook(Book(13, "Frankenstein", "Mary Shelley", 280))
library.addBook(Book(14, "The Da Vinci Code", "Dan Brown", 489))
library.addBook(Book(15, "The Catcher in the Rye", "J.D. Salinger", 234))

library.addStudent(Student(1, "Ali"))
library.addStudent(Student(2, "Ahmed"))
library.addStudent(Student(3, "Murad"))
library.addStudent(Student(4, "Leyla"))
library.addStudent(Student(5, "Aysel"))
library.addStudent(Student(6, "David"))
library.addStudent(Student(7, "James"))
library.addStudent(Student(8, "Michael"))
library.addStudent(Student(9, "Daniel"))
library.addStudent(Student(10, "Emily"))
library.addStudent(Student(11, "Sophia"))
library.addStudent(Student(12, "Olivia"))
library.addStudent(Student(13, "Emma"))
library.addStudent(Student(14, "William"))
library.addStudent(Student(15, "Alexander"))

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

    try:
        choice = input("Enter your choice: ")

        if choice == "1":

            bookID = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter author: ")
            pageCount = int(input("Enter page count: "))

            book = Book(bookID, title, author, pageCount)
            library.addBook(book)

            print("\nBook added successfully.")

        elif choice == "2":
        
            studentID = int(input("Enter student ID: "))
            name = input("Enter student name: ")

            student = Student(studentID, name)
            library.addStudent(student)

            print("\nStudent added successfully.")

        elif choice == "3":
            library.showBooks()

        elif choice == "4":
            library.showStudents()

        elif choice == "5":

            studentID = int(input("Enter student ID: "))
            bookID = int(input("Enter book ID: "))

            library.borrowBook(studentID, bookID)

        elif choice == "6":

            studentID = int(input("Enter student ID: "))
            bookID = int(input("Enter book ID: "))

            library.returnBook(studentID, bookID)

        elif choice == "7":
            print("\nExiting Library System...")
            break

        else:
            print("\nInvalid choice. Try again.")

    except ValueError:
        print("Please enter a valid number!")

    except Exception as e:
        print("An error occurred:", e)
