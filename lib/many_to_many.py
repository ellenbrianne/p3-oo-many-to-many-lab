class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)

    def contracts(self):
        c_list = [c for c in Contract.all if self.name == c.author]
        print(c_list)

    def books(self):
        pass

    def sign_contract(self, book, date, royalties):
        pass

    def total_royalties(self):
        pass


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self.all.append(self)

    def contracts_by_date(cls, date):
        pass


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception
        
author = Author("author")
book = Book("title")
contract = Contract(author, book, "01/01/2002", 100)
author.contracts()