class Client(object):
    def __init__(self, id: str, name: str):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __eq__(self, other):
        if type(other) != Client:
            return False
        return self.id == other.id

    def __str__(self):
        return f"Id: {self.__id}, Name: {self.__name}"

    def __repr__(self):
        return str(self)
