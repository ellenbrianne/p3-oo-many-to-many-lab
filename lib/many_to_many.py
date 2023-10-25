class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)

    # working, test != passing
    def contracts(self):
        c_list = [c for c in Contract.all if c.author.name == self.name] 
        return c_list
    
    def books(self):
        matching_c = [c for c in Contract.all if c.author.name == self.name]
        matching_b = []
        for b in Book.all:
            for c in matching_c:
                if b.title == c.book.title:
                    matching_b.append(b)
        return matching_b

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    # working, test != passing
    def total_royalties(self):
        c_list = self.contracts()
        r_list = [c.royalties for c in c_list]
        return sum(r_list)

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self.all.append(self)

    # working, test != passing
    def contracts(self):
        c_list = [c for c in Contract.all if self.title == c.book.title]
        return c_list

    def authors(self):
        matching_c = [c for c in Contract.all if c.book.title == self.title]
        matching_a = []
        for a in Author.all:
            for c in matching_c:
                if a.name == c.author.name:
                    matching_a.append(a)
        return matching_a

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
        c_list = Contract.all

        def myFunc(c):
            return c.date
        
        c_list.sort(key=myFunc)
        return c_list

    
# author = Author("name")

# author_2 = Author("name_2")

# book = Book("title")
# book_2 = Book("title_2")

# contract_1 = Contract(author, book, "02/16/2010", 10)
# contract_3 = Contract(author_2, book, "01/01/2005", 5)
# contract_2 = Contract(author, book_2, "01/15/2005", 15)
# contract_4 = Contract(author, book_2, "01/15/2005", 15)

# author.total_royalties()