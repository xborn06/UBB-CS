class Book(object):
    def __init__(self, id: str, author: str, title: str):
        self.__id = id
        self.__author = author
        self.__title = title

    @property
    def id(self):
        return self.__id

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @author.setter
    def author(self, new_author):
        self.__author = new_author

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    def __eq__(self, other):
        if type(other) != Book:
            return False
        return self.id == other.id

    def __str__(self):
        return f"Id: {self.id}, Author: {self.author}, Title: {self.title}"

    def __repr__(self):
        return str(self)
