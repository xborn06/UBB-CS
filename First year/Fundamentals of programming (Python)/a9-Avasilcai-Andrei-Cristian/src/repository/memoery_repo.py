class RepositoryError(Exception):
    """Base class for exceptions in the repository."""

    def __init__(self, message="A repository error occurred"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class DuplicateIDError(RepositoryError):
    """Raised when attempting to add an element with a duplicate ID."""

    def __init__(self, message="Duplicate object ID found"):
        super().__init__(message)

class DuplicateTitleError(RepositoryError):
    """Raised when attempting to add an element with a duplicate ID."""

    def __init__(self, message="Duplicate object title found"):
        super().__init__(message)

class DuplicateNameError(RepositoryError):
    def __init__(self,message = "Duplicate object name found"):
        super().__init__(message)

class IDNotFoundError(RepositoryError):
    """Raised when an element with a specified ID is not found in the repository."""

    def __init__(self, message="The specified ID was not found in the repository"):
        super().__init__(message)

class TitleNotFoundError(RepositoryError):
    """Raised when an element with a specified title is not found in the repository."""

    def __init__(self, message="The specified title was not found in the repository"):
        super().__init__(message)

class AuthorNotFoundError(RepositoryError):
    """Raised when an element with a specified author is not found in the repository."""

    def __init__(self, message="The specified author was not found in the repository"):
        super().__init__(message)

class NameNotFoundError(RepositoryError):
    """Raised when an element with a specified name is not found in the repository."""

    def __init__(self, message="The specified name was not found in the repository"):
        super().__init__(message)


class RepositoryIterator:
    def __init__(self, data):
        self.__data = data
        self.__pos = -1

    def __next__(self):
        self.__pos += 1
        if self.__pos >= len(self.__data):
            raise StopIteration()
        return self.__data[self.__pos]


class BookMemoryRepository:
    def __init__(self):
        self._data = {}
        self.history = []

    def save_state(self):
        """Save the current state of the repository."""
        self.history.append(self._data.copy())

    def add(self, book):
        """Add a new book if its ID is unique."""
        if book.id in self._data:
            raise DuplicateIDError(
                f"A book with ID {book.id} already exists.")
        if book.title in self._data:
            raise DuplicateTitleError(
                f"A book with the title: {book.title} already exists.")
        self.save_state()
        self._data[book.id] = book

    def remove(self, id: str):
        """Remove a book by its ID."""
        if id not in self._data:
            raise IDNotFoundError(
                f"Book with ID {id} not found in the repository.")
        self.save_state()
        removed_book = self._data.pop(id)

    def get_all(self):
        """Return a list of all books in the repository."""
        return list(self._data.values())


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

    def update_book(self, book_id: str, new_data: dict):
        """Update a book's details by ID."""
        if book_id not in self._data:
            raise IDNotFoundError(f"Book with ID '{book_id}' not found.")
        book = self._data[book_id]
        if 'author' in new_data and len(new_data['author'])>0:
            book.author = new_data['author']
        if 'title' in new_data and len(new_data['title'])>0:
            book.title = new_data['title']


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

class ClientMemoryRepository:
    def __init__(self):
        self._data = {}
        self.history = []

    def save_state(self):
        """Save the current state of the repository."""
        self.history.append(self._data.copy())

    def add(self, client):
        """Add a new client if its ID is unique."""
        if client.id in self._data:
            raise DuplicateIDError(
                f"A Client with ID {client.id} already exists.")
        if client.name in self._data:
            raise DuplicateNameError(
                f"A name with the name: {client.name} already exists.")
        self.save_state()
        self._data[client.id] = client

    def remove(self, id: str):
        """Remove a client by its ID."""
        if id not in self._data:
            raise IDNotFoundError(
                f"Client with ID {id} not found in the repository.")
        self.save_state()
        removed_client = self._data.pop(id)

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


    def __iter__(self):
        """Return an iterator for the clients in the repository."""
        return RepositoryIterator(list(self._data.values()))

    def __getitem__(self, item):
        if item not in self._data:
            return None
        return self._data[item]

    def __len__(self):
        """Return the number of clients in the repository."""
        return len(self._data)

class RentalMemoryRepository:
    def __init__(self):
        self._data = {}
        self.history = []

    def save_state(self):
        """Save the current state of the repository."""
        self.history.append(self._data.copy())

    def add(self, rental):
        """Add a new rental if its ID is unique."""
        if rental.id in self._data:
            raise DuplicateIDError(
                f"A rental with ID {rental.id} already exists.")
        self.save_state()
        self._data[rental.id] = rental

    def remove(self, id: str):
        """Remove a rental by its ID."""
        if id not in self._data:
            raise IDNotFoundError(
                f"Rental with ID {id} not found in the repository.")
        self.save_state()
        removed_rental = self._data.pop(id)

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
        """Return an iterator for the rentals in the repository."""
        return RepositoryIterator(list(self._data.values()))

    def __getitem__(self, item):
        if item not in self._data:
            return None
        return self._data[item]

    def __len__(self):
        """Return the number of rentals in the repository."""
        return len(self._data)