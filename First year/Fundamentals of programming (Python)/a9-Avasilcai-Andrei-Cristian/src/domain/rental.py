from datetime import date, timedelta
class Rental(object):
    def __init__(self, id: str, book_id: str, client_id: str, rented_date: date, return_date : date):
        self.__id = id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__return_date = return_date

    @property
    def id(self):
        return self.__id

    @property
    def book_id(self):
        return self.__book_id

    @property
    def client_id(self):
        return self.__client_id

    @property
    def rented_date(self):
        return self.__rented_date

    @property
    def return_date(self):
        return self.__return_date

    @rented_date.setter
    def rented_date(self, new_rented_date):
        self.__rented_date = new_rented_date

    @return_date.setter
    def return_date(self, new_return_date):
        self.__return_date = new_return_date

    def __len__(self):
        if self.__return_date is not None:
            return (self.__return_date - self.__rented_date).days + 1
        today = date.today()
        return (today - self.__rented_date).days + 1

    def __eq__(self, other):
        if type(other) != Rental:
            return False
        return self.id == other.id

    def __str__(self):
        from_date = self.__rented_date.strftime("%d/%m/%Y")
        to_date = self.__return_date.strftime("%d/%m/%Y")
        return f"Id: {self.__id}, Book: {self.__book_id}, Client: {self.__client_id}, from {from_date}, to {to_date}"

    def __repr__(self):
        return str(self)