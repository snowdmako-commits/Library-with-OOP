class Book:

    def __init__(self, bookID, title, author, pageCount):
        self.bookID = bookID
        self.title = title
        self.author = author
        self.pageCount = pageCount
        self.isAvailable = True


    def showInfo(self):

        print(f"""
        ID: {self.bookID}
        Title: {self.title}
        Author: {self.author}
        pageCount: {self.pageCount}
        """)

        if self.isAvailable:
            print("Status: Available.")
        else:
            print("Status: Borrowed.")


    def borrow(self):

        if self.isAvailable:
            self.isAvailable = False
            print(f"\n{self.title} borrowed.")
        else:
            print("\nThis book is already borrowed.")


    def returnBook(self):
        
        if not self.isAvailable:
            self.isAvailable = True
            print(f"\n{self.title} returned.")
        else:
            print("\nThis book is already in the library.")