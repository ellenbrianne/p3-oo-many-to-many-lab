class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)

    def contracts(self):
        c_list = [c for c in Contract.all if c.author.name == self.name]
        return c_list

    def books(self):
        b_list = [b for b in Book.all if self.name in self.contracts()]
        return b_list

    def sign_contract(self, book, date, royalties):
        pass

    def total_royalties(self):
        pass


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self.all.append(self)


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

    @classmethod    
    def contracts_by_date(cls):
        def helper(c):
            return c.date

        print(cls.all.sort(key=helper))

    
author = Author("name")
book = Book("title")
contract_1 = Contract(author, book, "02/16/2010", 10)
contract_2 = Contract(author, book, "01/15/2005", 15)