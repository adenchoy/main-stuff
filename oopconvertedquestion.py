class StockItem:
    def __init__(self, Title, DateAcquired, OnLoan):
        self.title = Title
        self.dateacq = DateAcquired
        self.loaned = OnLoan
    def __repr__(self) -> str:
        return self

    def ShowTitle(self):
        return self.title
    def ShowDateAcquired(self):
        return self.dateacq
    def ShowOnLoan(self):
        return self.loaned
class Book(StockItem):
    def __init__(self, Title, DateAcquired, OnLoan, Author, ISBN):
        super().__init__(Title, DateAcquired, OnLoan)   
        self.author = Author
        self.isbn = ISBN
    def ShowAuthor(self):
        return self.author
    def ShowISBN(self):
        return self.isbn
NewBook = Book("Computers", "12/11/2001",False,"A.Nyone", "099111")
print(NewBook.ShowISBN())
