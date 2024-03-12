class Book:
    def __init__(self,title,author,publication_year):
        self.title = title
        self.author = author 
        self.publication_year = publication_year

book1 = Book("Война и мир","Лев Толстой",1867)
book2 = Book("WSPA","STUDENT",2024)

print(book1.title, book1.author, book1.publication_year)
print(book2.title, book2.author, book2.publication_year)
