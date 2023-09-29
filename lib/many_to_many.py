class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        pass

    def books(self):
        pass

    def sign_contract(self, book, date, royalties):
        pass

    def total_royalties(self):
        pass


class Book:
    def __init__(self, title):
        self.title = title

    def contracts_by_date(cls, date):
        pass


class Contract:
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

    def get_author(self):
        return self._author

    def set_author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception
        
    author = property(get_author, set_author)