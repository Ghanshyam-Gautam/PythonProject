#a book, which has a title,an author,which has a name. A method in author called write
#,which takes a book and prints"{author} is writing {book}"

class Book:
    def __init__(self,title):
        self.title=title

class Author:
    def __init__(self,name):
        self.name=name

    def writes(self,book):
        print(f"{self.name} is writing {book.title}")

s1=Book("Ramayan")
t1=Author("Balmiki")

t1.writes(s1)