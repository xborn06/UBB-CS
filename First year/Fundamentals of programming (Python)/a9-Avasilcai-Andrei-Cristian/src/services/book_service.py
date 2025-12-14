from src.domain.book import Book
from src.repository.memoery_repo import IDNotFoundError,  DuplicateIDError, TitleNotFoundError,AuthorNotFoundError

class IDValidatorException(KeyError):
    def __init__(self, message="A validation error occurred"):
        super().__init__(message)
        self.message = message

class ValidationException(Exception):
    def __init__(self, message = "A validation error occurred"):
        super().__init__(message)
        self.message = message

class BookService:
    def __init__(self, repo):
        """
        The repo parameter is the repository passed from outside (e.g., MemoryRepository)
        :param repo: Repository-like object that implements the necessary methods
        """
        self._repo = repo
        self._undo_stack = []
        self._redo_stack = []

    def add_book(self, id: str, author: str, title: str):
        """
        Adds a book to the repository. Returns a success or error message.
        :param id: the unique identifier
        :param author: the author of the book
        :param title: the title of the book
        :return: success or error message
        """
        book = Book(id, author, title)
        try:
            self._repo.add(book)
            self._redo_stack.clear()
            self._undo_stack.append(("remove", id, author, title))
            return "Book added successfully."
        except DuplicateIDError:
            return f"Error: Book with ID {id} already exists."
        except ValidationException as e:
            return f"Error: {str(e)}"

    def add_book_undo(self, id: str, author: str, title: str):
        """
        Adds a book to the repository. Returns a success or error message.
        :param id: the unique identifier
        :param author: the author of the book
        :param title: the title of the book
        :return: success or error message
        """
        book = Book(id, author, title)
        try:
            self._repo.add(book)
            return "Book added successfully."
        except DuplicateIDError:
            return f"Error: Book with ID {id} already exists."
        except ValidationException as e:
            return f"Error: {str(e)}"

    def add_book_redo(self, id: str, author: str, title: str):
        """
        Adds a book to the repository. Returns a success or error message.
        :param id: the unique identifier
        :param author: the author of the book
        :param title: the title of the book
        :return: success or error message
        """
        book = Book(id, author, title)
        try:
            self._repo.add(book)
            self._undo_stack.append(("remove", id, author, title))
            return "Book added successfully."
        except DuplicateIDError:
            return f"Error: Book with ID {id} already exists."
        except ValidationException as e:
            return f"Error: {str(e)}"

    def remove_book(self, id: str, rental_list: list,rental_repo):
        """
        Remove a book from the collection based on its unique identifier.
        :param rental_list:
        :param rental_repo:
        :param id: Unique identifier for the book that needs to be removed.
        :return:
        """
        try:
            book_to_remove = self._repo[id]
            if not book_to_remove:
                raise IDNotFoundError(f"No book found with ID: {id}")
            if rental_list:
                associated_rentals = [rental for rental in rental_list if rental.book_id == id]
            else :
                associated_rentals = []
            self._undo_stack.append(("add", id, book_to_remove, associated_rentals, rental_repo))
            self._repo.remove(id)
            for rental in associated_rentals:
                rental_repo.remove(rental.id)
            self._redo_stack.clear()
            return "Book removed successfully."
        except IDNotFoundError as ve:
            return f"Error: Book with ID {id} not found"

    def remove_book_undo(self, id: str, rental_list: list,rental_repo):
        """
        Remove a book from the collection based on its unique identifier.
        :param rental_list:
        :param rental_repo:
        :param id: Unique identifier for the book that needs to be removed.
        :return:
        """
        try:
            book_to_remove = self._repo[id]
            if not book_to_remove:
                raise IDNotFoundError(f"No book found with ID: {id}")
            if rental_list:
                associated_rentals = [rental for rental in rental_list if rental.book_id == id]
            else :
                associated_rentals = []
            self._repo.remove(id)
            for rental in associated_rentals:
                rental_repo.remove(rental.id)
            return "Book removed successfully."
        except IDNotFoundError as ve:
            return f"Error: Book with ID {id} not found"

    def remove_book_redo(self, id: str, rental_list: list,rental_repo):
        """
        Remove a book from the collection based on its unique identifier.
        :param rental_list:
        :param rental_repo:
        :param id: Unique identifier for the book that needs to be removed.
        :return:
        """
        try:
            book_to_remove = self._repo[id]
            if not book_to_remove:
                raise IDNotFoundError(f"No book found with ID: {id}")
            if rental_list:
                associated_rentals = [rental for rental in rental_list if rental.book_id == id]
            else :
                associated_rentals = []
            self._undo_stack.append(("add", id, book_to_remove, associated_rentals, rental_repo))
            self._repo.remove(id)
            for rental in associated_rentals:
                rental_repo.remove(rental.id)
            return "Book removed successfully."
        except IDNotFoundError as ve:
            return f"Error: Book with ID {id} not found"

    def get_all(self) -> list:
        """
        Returns a list with all the books in the repository.
        :return: list of all books
        """
        return self._repo.get_all()

    def find(self,find_type: int, user_input: str):
        """
        Finds a book in the repo based on id/title/author
        :param find_type:
        :param user_input:
        :return:
        """
        if find_type == 1:
            try:
                return self._repo.find_by_id(user_input)
            except IDNotFoundError as ve:
                return f"Error: {str(ve)}"
        elif find_type == 2:
            try:
                return self._repo.find_by_title(user_input)
            except TitleNotFoundError as ve:
                return f"Error: {str(ve)}"
        elif find_type == 3:
            try:
                return self._repo.find_by_author(user_input)
            except AuthorNotFoundError as ve:
                return f"Error: {str(ve)}"

    def update(self, new_data, id):
        """
        Updates a book's information (title, author)
        :param new_data:
        :param id:
        :return:
        """
        try:
            book_to_update = self._repo._data[id]
            original_data = {
                "author": book_to_update.author,
                "title": book_to_update.title,
            }
            self._undo_stack.append(("update", id, original_data))
            self._repo.update_book(id, new_data)
            return "Book updated successfully."
        except IDNotFoundError as idnfe:
            return f"Error: {str(idnfe)}"
        except ValidationException as ve:
            return f"Error: {str(ve)}"

    def update_undo(self, new_data, id):
        """
        Updates a book's information (title, author)
        :param new_data:
        :param id:
        :return:
        """
        try:
            book_to_update = self._repo._data[id]
            self._repo.update_book(id, new_data)
            return "Book updated successfully."
        except IDNotFoundError as idnfe:
            return f"Error: {str(idnfe)}"
        except ValidationException as ve:
            return f"Error: {str(ve)}"

    def update_redo(self, new_data, id):
        """
        Updates a book's information (title, author)
        :param new_data:
        :param id:
        :return:
        """
        try:
            book_to_update = self._repo._data[id]
            original_data = {
                "author": book_to_update.author,
                "title": book_to_update.title,
            }
            self._undo_stack.append(("update", id, original_data))
            self._repo.update_book(id, new_data)
            self._redo_stack.clear()
            return "Book updated successfully."
        except IDNotFoundError as idnfe:
            return f"Error: {str(idnfe)}"
        except ValidationException as ve:
            return f"Error: {str(ve)}"

    def undo_action(self):
        if not self._undo_stack:
            raise Exception("No actions to undo!")
        action = self._undo_stack.pop()
        if action[0] == "add":
            book_id, book, related_rentals, rental_repo = action[1], action[2], action[3], action[4]
            self.add_book_undo(book_id, book.author, book.title)
            for rental in related_rentals:
                rental_repo.add(rental)
            self._redo_stack.append(("remove", book_id, related_rentals, rental_repo))
        elif action[0] == "remove":
            book_id = action[1]
            book_title = action[2]
            book_author = action[3]
            self.remove_book_undo(book_id, [], [])
            self._redo_stack.append(("add",book_id, book_author, book_title))
        elif action[0] == "update":
            book_id, original_data = action[1], action[2]
            new_data = {
                'author': self._repo._data[book_id].author,
                'title': self._repo._data[book_id].title
            }
            self.update_undo(original_data, book_id)
            self._redo_stack.append(("update", book_id, new_data))
    def redo_action(self):
        if not self._redo_stack:
            raise Exception("No actions to redo!")
        action = self._redo_stack.pop()
        if action[0] == "add":
            book_id, book_author, book_title = action[1], action[2], action[3]
            self.add_book_redo(book_id, book_author, book_title)
        elif action[0] == "remove":
            book_id = action[1]
            related_rentals = action[2]
            rental_repo = action[3]
            self.remove_book_redo(book_id, related_rentals, rental_repo)
        elif action[0] == "update":
            book_id, new_data = action[1], action[2]
            self.update_redo(new_data, book_id)





