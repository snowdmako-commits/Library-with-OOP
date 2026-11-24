# 📚 Library Management System

A simple and interactive **Library Management System** built with Python and Object-Oriented Programming (OOP).

This project allows users to manage books and students, borrow books, and return borrowed books through a simple menu-based interface.

---

## 🚀 Features

- 📖 **Show Books** – Display all available books in the library.
- 👨‍🎓 **Show Students** – Display all registered students.
- 📕 **Borrow Book** – Allow students to borrow books.
- 📗 **Return Book** – Allow students to return borrowed books.
- 🔍 **Search Book** – Find books using their ID.
- 🔍 **Search Student** – Find students using their ID.
- ⚠️ **Availability Check** – Prevent borrowing books that are already borrowed.
- 🔄 **Automatic Status Update** – Update book availability when borrowed or returned.

---

## 🛠️ Technologies Used

- 🐍 Python 3
- 🧱 Object-Oriented Programming (OOP)
- 📦 Python Classes and Objects
- 📋 Lists
- 🔁 Loops and Conditional Statements
- ⚙️ Methods and Constructors

---

## 📂 Project Structure

```text
Library-Management-System/
│
├── main.py
├── book.py
├── student.py
├── library.py
└── README.md
```

### 📄 File Descriptions

| File | Description |
|---|---|
| `main.py` | Main program and menu system |
| `book.py` | Book class and book operations |
| `student.py` | Student class and borrowing operations |
| `library.py` | Library management and system operations |
| `README.md` | Project documentation |

---

## 🧱 Classes and Responsibilities

### 1️⃣ Book Class

The `Book` class represents a book in the library.

**Attributes:**
- `bookID` – Unique ID of the book.
- `title` – Book title.
- `author` – Book author.
- `pageCount` – Number of pages.
- `isAvailable` – Availability status of the book.

**Methods:**
- `showInfo()` – Displays book information.
- `borrow()` – Changes the book status to borrowed.
- `returnBook()` – Changes the book status to available.

### 2️⃣ Student Class

The `Student` class represents a registered student.

**Attributes:**
- `studentID` – Unique ID of the student.
- `name` – Student name.
- `borrowedBooks` – List of books borrowed by the student.

**Methods:**
- `showInfo()` – Displays student information.
- `borrowBook()` – Allows a student to borrow a book.
- `returnBook()` – Allows a student to return a book.

### 3️⃣ Library Class

The `Library` class manages books and students.

**Attributes:**
- `name` – Library name.
- `books` – List of books.
- `students` – List of students.

**Methods:**
- `addBook()` – Adds a book to the library.
- `addStudent()` – Registers a student.
- `showBooks()` – Displays all books.
- `showStudents()` – Displays all students.
- `searchBook()` – Searches for a book by ID.
- `searchStudent()` – Searches for a student by ID.
- `borrowBook()` – Manages the borrowing process.
- `returnBook()` – Manages the returning process.

---

## ⚙️ How to Run

**1. Clone the repository**

```bash
git clone https://github.com/your-username/Library-Management-System.git
```

**2. Open the project folder**

```bash
cd Library-Management-System
```

**3. Run the program**

```bash
python main.py
```

---

## 🎮 Menu Options

When you run the program, you will see the following menu:

```text
========== LIBRARY SYSTEM ==========

1. Show Books
2. Show Students
3. Borrow Book
4. Return Book
5. Exit

====================================
```

### 📌 Example Usage

**Borrowing a book:**

```text
Enter your choice: 3

Enter student ID: 1
Enter book ID: 2

The Hobbit borrowed.
```

**Returning a book:**

```text
Enter your choice: 4

Enter student ID: 1
Enter book ID: 2

The Hobbit returned.
```

---

## 🧠 What I Learned

Through this project, I practiced:

- Understanding Object-Oriented Programming (OOP).
- Creating and working with classes and objects.
- Using constructors (`__init__`).
- Understanding `self` and object attributes.
- Working with lists and dictionaries.
- Using methods to organize code.
- Implementing relationships between different classes.
- Managing data between multiple Python files.
- Practicing modular programming.

---

## 🔮 Future Improvements

Possible improvements for this project:

- 💾 Save books and students using JSON.
- ➕ Add new books dynamically.
- ➕ Register new students.
- 🗑️ Remove books and students.
- 🔎 Add search by book title or student name.
- 📊 Add borrowing history.
- 📅 Add borrowing dates and return deadlines.
- 🔐 Add an administrator system.

---

## 👨‍💻 Author

**Your Name**

Python Developer | Learning Object-Oriented Programming

---

⭐ If you like this project, don't forget to give it a star!

**Thank you for checking out my Library Management System! 📚**
