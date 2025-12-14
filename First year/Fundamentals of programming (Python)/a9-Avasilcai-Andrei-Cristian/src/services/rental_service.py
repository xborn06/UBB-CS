from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
from datetime import datetime

from src.repository.memoery_repo import IDNotFoundError

dt = datetime.now()

class InvalidDateFromat(ValueError):
    def __init__(self, message="A date format error occurred"):
        super().__init__(message)
        self.message = message

class IDValidatorException(KeyError):
    def __init__(self, message="A validation error occurred"):
        super().__init__(message)
        self.message = message

class ValidationException(Exception):
    def __init__(self, message = "A validation error occurred"):
        super().__init__(message)
        self.message = message

class RentalService:
    def __init__(self, repo):
        """
        The repo parameter is the repository passed from outside (e.g., MemoryRepository)
        :param repo: Repository-like object that implements the necessary methods
        """
        self._repo = repo
        self._undo_stack = []
        self._redo_stack = []

    @property
    def repo(self):
        return self._repo

    def is_book_available(self, book_id, start_date, end_date):
        """Check if a book is available for rental during the given dates."""
        for rental in self._repo.get_all():
            if rental.book_id == book_id:
                if (end_date >= rental.rented_date and end_date <= rental.return_date) or (start_date <= rental.return_date and start_date >= rental.rented_date):
                    return False
        return True

    def add_rental(self, id: str, book_id: str, client_id: str, rented_date: str, return_date : str, booklist, clientlist):
        """
        Adds a rental to the repository
        :param clientlist:
        :param booklist:
        :param id:
        :param book_id:
        :param client_id:
        :param rented_date:
        :param return_date:
        :return:
        """
        if not any(book.id == book_id for book in booklist):
            return f"Error: Book with ID {book_id} not found"
        if not any(client.id == client_id for client in clientlist):
            return f"Error: Client with ID {client_id} not found"
        try:
            if type(rented_date) == str:
                rented_date = datetime.strptime(rented_date, "%d/%m/%Y").date()
            if type(return_date) == str:
                return_date = datetime.strptime(return_date, "%d/%m/%Y").date()
            if rented_date > return_date:
                return "Error: Rented date cannot be after return date."
            if self.is_book_available(book_id, rented_date, return_date):
                rental = Rental(id, book_id, client_id, rented_date, return_date)
                self._repo.add(rental)
                self._undo_stack.append(("remove", id))
                self._redo_stack.clear()
                return "Rental added successfully."
            else:
                return f"Error: Book with ID {book_id} is not available for rental."
        except IDValidatorException:
            return f"Error: Rental with ID {id} already exists."
        except ValidationException as e:
            return f"Error: {str(e)}"
        except InvalidDateFromat as ide :
            return "Error: Invalid date format. Use the following format: DD/MM/YYYY."

    def add_rental_undo(self, id: str, book_id: str, client_id: str, rented_date: str, return_date : str, booklist, clientlist):
        """
        Adds a rental to the repository
        :param clientlist:
        :param booklist:
        :param id:
        :param book_id:
        :param client_id:
        :param rented_date:
        :param return_date:
        :return:
        """
        if not any(book.id == book_id for book in booklist):
            return f"Error: Book with ID {book_id} not found"
        if not any(client.id == client_id for client in clientlist):
            return f"Error: Client with ID {client_id} not found"
        try:
            if type(rented_date) == str:
                rented_date = datetime.strptime(rented_date, "%d/%m/%Y").date()
            if type(return_date) == str:
                return_date = datetime.strptime(return_date, "%d/%m/%Y").date()
            if rented_date > return_date:
                return "Error: Rented date cannot be after return date."
            if self.is_book_available(book_id, rented_date, return_date):
                rental = Rental(id, book_id, client_id, rented_date, return_date)
                self._repo.add(rental)
                return "Rental added successfully."
            else:
                return f"Error: Book with ID {book_id} is not available for rental."
        except IDValidatorException:
            return f"Error: Rental with ID {id} already exists."
        except ValidationException as e:
            return f"Error: {str(e)}"
        except InvalidDateFromat as ide :
            return "Error: Invalid date format. Use the following format: DD/MM/YYYY."

    def add_rental_redo(self, id: str, book_id: str, client_id: str, rented_date: str, return_date : str, booklist, clientlist):
        """
        Adds a rental to the repository
        :param clientlist:
        :param booklist:
        :param id:
        :param book_id:
        :param client_id:
        :param rented_date:
        :param return_date:
        :return:
        """
        if not any(book.id == book_id for book in booklist):
            return f"Error: Book with ID {book_id} not found"
        if not any(client.id == client_id for client in clientlist):
            return f"Error: Client with ID {client_id} not found"
        try:
            if type(rented_date) == str:
                rented_date = datetime.strptime(rented_date, "%d/%m/%Y").date()
            if type(return_date) == str:
                return_date = datetime.strptime(return_date, "%d/%m/%Y").date()
            if rented_date > return_date:
                return "Error: Rented date cannot be after return date."
            if self.is_book_available(book_id, rented_date, return_date):
                rental = Rental(id, book_id, client_id, rented_date, return_date)
                self._repo.add(rental)
                self._undo_stack.append(("remove", id))
                return "Rental added successfully."
            else:
                return f"Error: Book with ID {book_id} is not available for rental."
        except IDValidatorException:
            return f"Error: Rental with ID {id} already exists."
        except ValidationException as e:
            return f"Error: {str(e)}"
        except InvalidDateFromat as ide :
            return "Error: Invalid date format. Use the following format: DD/MM/YYYY."

    def remove_rental(self, id: str):
        """
        Remove a rental from the collection based on its unique identifier.
        :param id: Unique identifier for the rental that needs to be removed.
        :return:
        """
        try:
            rental_to_remove = self._repo[id]
            self._repo.remove(id)
            self._undo_stack.append(("add", id, rental_to_remove.book_id, rental_to_remove.client_id, rental_to_remove.rented_date, rental_to_remove.return_date, [Book(rental_to_remove.book_id,"","")], [Client(rental_to_remove.client_id,"")]))
            self._redo_stack.clear()
            return "Rental removed successfully."
        except IDValidatorException:
            return f"Error: Rental with ID {id} not found"
        except IDNotFoundError as idnfe:
            return f"Error: {str(idnfe)}"

    def remove_rental_undo(self, id: str):
        """
        Remove a rental from the collection based on its unique identifier.
        :param id: Unique identifier for the rental that needs to be removed.
        :return:
        """
        try:
            self._repo.remove(id)
            return "Rental removed successfully."
        except IDValidatorException:
            return f"Error: Rental with ID {id} not found"
        except IDNotFoundError as idnfe:
            return f"Error: {str(idnfe)}"

    def remove_rental_redo(self, id: str):
        """
        Remove a rental from the collection based on its unique identifier.
        :param id: Unique identifier for the rental that needs to be removed.
        :return:
        """
        try:
            rental_to_remove = self._repo[id]
            self._repo.remove(id)
            self._undo_stack.append(("add", id, rental_to_remove.book_id, rental_to_remove.client_id, rental_to_remove.rented_date, rental_to_remove.return_date, [Book(rental_to_remove.book_id,"","")], [Client(rental_to_remove.client_id,"")]))
            return "Rental removed successfully."
        except IDValidatorException:
            return f"Error: Rental with ID {id} not found"
        except IDNotFoundError as idnfe:
            return f"Error: {str(idnfe)}"

    def get_all(self) -> list:
        """
        Returns a list with all the rentals in the repository.
        :return: list of all clients
        """
        return self._repo.get_all()

    def undo_action(self):
        if not self._undo_stack:
            raise Exception("No actions to undo!")
        action = self._undo_stack.pop()
        if action[0] == "add":
            rental_id, book_id, client_id, rented_date, return_date, booklist, clientlist = action[1], action[2], action[3], action[4], action[5], action[6], action[7]
            self.add_rental_undo(rental_id, book_id, client_id, rented_date, return_date, booklist, clientlist)
            self._redo_stack.append(("remove", rental_id))
        elif action[0] == "remove":
            rental_id = action[1]
            self._redo_stack.append(("add", rental_id, self._repo[rental_id].book_id, self._repo[rental_id].client_id,
                                     self._repo[rental_id].rented_date, self._repo[rental_id].return_date,
                                     [Book(self._repo[rental_id].book_id, "", "")],
                                     [Client(self._repo[rental_id].client_id, "")]))
            self.remove_rental_undo(rental_id)

    def redo_action(self):
        if not self._redo_stack:
            raise Exception("No actions to redo!")
        action = self._redo_stack.pop()
        if action[0] == "add":
            rental_id, book_id, client_id, rented_date, return_date, booklist, clientlist = action[1], action[2], action[3], action[4], action[5], action[6], action[7]
            self.add_rental_redo(rental_id, book_id, client_id, rented_date, return_date, booklist, clientlist)
            self._undo_stack.append(("remove",rental_id))
        elif action[0] == "remove":
            rental_id = action[1]
            self.remove_rental_redo(rental_id)

    def get_most_rented_books(self, book_repo):
        """Get the list of books sorted by the number of times they were rented (descending)."""
        rental_count = {}
        for rental in self._repo.get_all():
            book_id = rental.book_id
            if book_id in rental_count:
                rental_count[book_id] += 1
            else:
                rental_count[book_id] = 1
        books_with_rental_count = []
        for book_id, count in rental_count.items():
            if book_id in book_repo._data:
                book = book_repo._data[book_id]
                books_with_rental_count.append((book, count))
        sorted_books = sorted(books_with_rental_count, key=lambda x: x[1], reverse=True)
        return [(book, count) for book, count in sorted_books]

    def get_most_active_clients(self):
        """Get the list of clients sorted by total rental days (descending)."""
        client_rental_days = {}
        for rental in self._repo.get_all():
            rental_days = len(rental)
            client_id = rental.client_id
            client_rental_days[client_id] = client_rental_days.get(client_id, 0) + rental_days
        sorted_clients = sorted(client_rental_days.items(), key=lambda x: x[1], reverse=True)
        return sorted_clients

    def get_most_rented_authors(self, book_repo):
        """Get the list of authors sorted by the number of rentals (descending)."""
        book_to_author = {}
        for book in book_repo.get_all():
            book_to_author[book.id] = book.author
        author_rental_count = {}
        for rental in self._repo.get_all():
            book_id = rental.book_id
            if book_id in book_to_author:
                author = book_to_author[book_id]
                author_rental_count[author] = author_rental_count.get(author, 0) + 1
        sorted_authors = sorted(author_rental_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_authors
