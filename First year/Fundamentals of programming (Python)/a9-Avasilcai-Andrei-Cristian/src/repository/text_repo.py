from datetime import datetime

from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
from src.repository.memoery_repo import IDNotFoundError, DuplicateIDError, DuplicateNameError, \
    DuplicateTitleError, AuthorNotFoundError, TitleNotFoundError, RepositoryIterator, NameNotFoundError, RepositoryError


class BookFileRepository:
    def __init__(self, file_path):
        self._file_path = file_path
        self._data = {}
        self._history = []
        self._load_data()

    def _load_data(self):
        try:
            with open(self._file_path, 'r') as file:
                for line in file:
                    if not line.strip():
                        continue
                    parts = line.strip().split(', ')
                    if len(parts) == 3:
                        book_id, author, title = parts
                        self._data[book_id] = Book(book_id, author, title)
        except FileNotFoundError:
            print(f"File {self._file_path} not found. Repository initialized empty.")

    def _save_data(self):
        with open(self._file_path, 'w') as file:
            for book in self._data.values():
                file.write(f"{book.id}, {book.author}, {book.title}\n")

    def add(self, book):
        """Add a new book if its ID is unique."""
        if book.id in self._data:
            raise DuplicateIDError(
                f"A book with ID {book.id} already exists.")
        if book.title in self._data:
            raise DuplicateTitleError(
                f"A book with the title: {book.title} already exists.")
        self._data[book.id] = book
        self._save_data()

    def remove(self, book_id: str):
        """Remove a book by its ID."""
        if id not in self._data:
            raise IDNotFoundError(
                f"Book with ID {id} not found in the repository.")
        removed_book = self._data.pop(book_id)
        self._save_data()

    def get_all(self):
        """Return a list of all books in the repository."""
        return list(self._data.values())

    def update_book(self, book_id: str, new_data: dict):
        """Update a book's details by ID."""
        if book_id not in self._data:
            raise IDNotFoundError(f"Book with ID '{book_id}' not found.")
        book = self._data[book_id]
        if 'author' in new_data and len(new_data['author'])>0:
            book.author = new_data['author']
        if 'title' in new_data and len(new_data['title'])>0:
            book.title = new_data['title']
        self._save_data()

    def find_by_id(self, id: str):
        """Find books by partial ID matching."""
        id = id.lower().strip()
        matches = {key: value for key, value in self._data.items() if id in value.id.lower()}
        if not matches:
            raise IDNotFoundError(
                f"No books found with ID containing '{id}' in the repository.")
        return matches

    def find_by_author(self, author: str):
        """Find books by partial author name matching."""
        author = author.lower().strip()
        matches = {key: value for key, value in self._data.items() if author in value.author.lower()}
        if not matches:
            raise AuthorNotFoundError(
                f"No books found with author containing '{author}' in the repository.")
        return matches

    def find_by_title(self, title: str):
        """Find books by partial title matching."""
        title = title.strip().lower()
        matches = {key: value for key, value in self._data.items() if title in value.title.lower()}
        if not matches:
            raise TitleNotFoundError(
                f"No books found with title containing '{title}' in the repository.")
        return matches

    def __iter__(self):
        """Return an iterator for the books in the repository."""
        return RepositoryIterator(list(self._data.values()))

    def __getitem__(self, item):
        if item not in self._data:
            return None
        return self._data[item]

    def __len__(self):
        """Return the number of books in the repository."""
        return len(self._data)

class ClientFileRepository:
    def __init__(self, file_path):
        self._file_path = file_path
        self._data = {}
        self._history = []
        self._load_data()

    def _load_data(self):
        try:
            with open(self._file_path, 'r') as file:
                for line in file:
                    if not line.strip():
                        continue
                    parts = line.strip().split(', ')
                    if len(parts) == 2:
                        client_id, name = parts
                        self._data[client_id] = Client(client_id, name)
        except FileNotFoundError:
            print(f"File {self._file_path} not found. Repository initialized empty.")

    def _save_data(self):
        with open(self._file_path, 'w') as file:
            for client in self._data.values():
                file.write(f"{client.id}, {client.name}\n")


    def add(self, client):
        """Add a new client if its ID is unique."""
        if client.id in self._data:
            raise DuplicateIDError(
                f"A Client with ID {client.id} already exists.")
        if client.name in self._data:
            raise DuplicateNameError(
                f"A name with the name: {client.name} already exists.")
        self._data[client.id] = client
        self._save_data()

    def remove(self, client_id: str):
        """Remove a client by its ID."""
        if client_id not in self._data:
            raise IDNotFoundError(f"Client with ID {client_id} not found.")
        removed_client = self._data.pop(client_id)
        self._save_data()

    def get_all(self):
        """Return a list of all clients in the repository."""
        return list(self._data.values())

    def find_by_id(self, id: str):
        """Find clients by partial ID matching."""
        id = id.lower().strip()
        matches = {key: value for key, value in self._data.items() if id in value.id.lower()}
        if not matches:
            raise IDNotFoundError(
                f"No clients found with ID containing '{id}' in the repository.")
        return matches

    def find_by_name(self, name: str):
        """Find clients by partial name matching."""
        name = name.lower().strip()
        matches = {key: value for key, value in self._data.items() if name in value.name.lower()}
        if not matches:
            raise NameNotFoundError(
                f"No client found with the name '{name}' in the repository.")
        return matches

    def update_client(self, client_id: str, new_data: dict):
        """Update a client's details by ID."""
        if client_id not in self._data:
                raise IDNotFoundError(f"Client with ID '{client_id}' not found.")
        client = self._data[client_id]
        if 'name' in new_data and len(new_data['name'])>0:
            client.name = new_data['name']
        self._save_data()



    def __iter__(self):
        return iter(self._data.values())

    def __getitem__(self, item):
        return self._data.get(item)

    def __len__(self):
        return len(self._data)

class RentalFileRepository:
    def __init__(self, file_path):
        self._file_path = file_path
        self._data = {}
        self._history = []
        self._load_data()

    def _load_data(self):
        """
        Loads from file
        :return:
        """
        try:
            with open(self._file_path, 'r') as file:
                for line in file:
                    if not line.strip():
                        continue
                    parts = line.strip().split(', ')
                    if len(parts) == 5:
                        rental_id, client_id, book_id, rented_date, return_date = parts
                        rented_date = datetime.strptime(rented_date, "%d/%m/%Y")
                        return_date = datetime.strptime(return_date, "%d/%m/%Y")
                        self._data[rental_id] = Rental(rental_id, client_id, book_id, rented_date, return_date)
        except FileNotFoundError:
            print(f"File {self._file_path} not found. Repository initialized empty.")

    def _save_data(self):
        with open(self._file_path, 'w') as file:
            for rental in self._data.values():
                r1 = rental.rented_date.strftime("%d/%m/%Y")
                r2 = rental.return_date.strftime("%d/%m/%Y")
                file.write(f"{rental.id}, {rental.book_id}, {rental.client_id}, {r1}, {r2}\n")

    def add(self, rental):
        """Add a new rental if its ID is unique."""
        if rental.id in self._data:
            raise DuplicateIDError(
                f"A rental with ID {rental.id} already exists.")
        self._data[rental.id] = rental
        self._save_data()

    def remove(self, rental_id: str):
        """Remove a rental by its ID."""
        if rental_id not in self._data:
            raise IDNotFoundError(f"Rental with ID {rental_id} not found.")
        removed_rental = self._data.pop(rental_id)
        self._save_data()

    def get_all(self):
        """Return a list of all rentals in the repository."""
        return list(self._data.values())


    def find_by_id(self, id: str):
        """Find rentals by partial ID matching."""
        id = id.strip().lower()
        matches = {key: value for key, value in self._data.items() if id in value.id.lower()}
        if not matches:
            raise IDNotFoundError(
                f"No rentals found with ID containing '{id}' in the repository.")
        return matches

    def get_last_rental_id(self):
        """Return the ID of the last rental added to the repository."""
        if not self._data:
            raise RepositoryError("No rentals in the repository.")
        last_rental_id = list(self._data.keys())[-1]
        return last_rental_id

    def __iter__(self):
        return iter(self._data.values())

    def __getitem__(self, item):
        return self._data.get(item)

    def __len__(self):
        return len(self._data)
