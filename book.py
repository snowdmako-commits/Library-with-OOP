class Book:

    def __init__(self, bookID, title, author, pageCount):
        self.bookID = bookID
        self.title = title
        self.author = author
        self.pageCount = pageCount
        self.isAvailable = True