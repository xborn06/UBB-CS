import unittest
from src.domain.book import Book
from src.domain.client import Client
from src.repository.memoery_repo import BookMemoryRepository, ClientMemoryRepository
from src.repository.memoery_repo import DuplicateIDError, IDNotFoundError
from unittest.mock import MagicMock
from src.services.book_service import BookService
from src.services.client_service import ClientService
from src.services.client_service import DuplicateIDError


class TestBookMemoryRepository(unittest.TestCase):

    def setUp(self):
        self.repo = BookMemoryRepository()
        self.book1 = Book("01", "Title One", "Author A")
        self.book2 = Book("02", "Title Two", "Author B")

    def test_add_book(self):
        self.repo.add(self.book1)
        self.assertIn(self.book1.id, self.repo._data)

    def test_duplicate_id(self):
        self.repo.add(self.book1)
        with self.assertRaises(DuplicateIDError):
            self.repo.add(self.book1)  # Adding same ID again

    def test_remove_book(self):
        self.repo.add(self.book1)
        self.repo.remove(self.book1.id)
        self.assertNotIn(self.book1.id, self.repo._data)

    def test_remove_nonexistent_book(self):
        with self.assertRaises(IDNotFoundError):
            self.repo.remove("nonexistent_id")

    def test_update_book(self):
        self.repo.add(self.book1)
        self.repo.update_book(self.book1.id, {"title": "New Title", "author": "New Author"})
        updated_book = self.repo._data[self.book1.id]
        self.assertEqual(updated_book.title, "New Title")
        self.assertEqual(updated_book.author, "New Author")


class TestClientMemoryRepository(unittest.TestCase):

    def setUp(self):
        self.repo = ClientMemoryRepository()
        self.client1 = Client("01", "Client One")
        self.client2 = Client("02", "Client Two")

    def test_add_client(self):
        self.repo.add(self.client1)
        self.assertIn(self.client1.id, self.repo._data)

    def test_duplicate_client_id(self):
        self.repo.add(self.client1)
        with self.assertRaises(DuplicateIDError):
            self.repo.add(self.client1)  # Adding same ID again

    def test_remove_client(self):
        self.repo.add(self.client1)
        self.repo.remove(self.client1.id)
        self.assertNotIn(self.client1.id, self.repo._data)

    def test_remove_nonexistent_client(self):
        with self.assertRaises(IDNotFoundError):
            self.repo.remove("nonexistent_id")

    def test_update_client(self):
        self.repo.add(self.client1)
        self.repo.update_client(self.client1.id, {"name": "New Client Name"})
        updated_client = self.repo._data[self.client1.id]
        self.assertEqual(updated_client.name, "New Client Name")

class TestBookService(unittest.TestCase):

    def setUp(self):
        self.repo = MagicMock()
        self.service = BookService(self.repo)

    def test_add_book_success(self):
        self.repo.add = MagicMock()
        result = self.service.add_book("1", "Author A", "Title A")
        self.assertEqual(result, "Book added successfully.")
        self.repo.add.assert_called_once()

    def test_add_book_duplicate_id(self):
        self.repo.add.side_effect = DuplicateIDError
        result = self.service.add_book("1", "Author A", "Title A")
        self.assertEqual(result, "Error: Book with ID 1 already exists.")

    def test_remove_book_success(self):
        self.repo.remove = MagicMock()
        result = self.service.remove_book("1", [],self.repo)
        self.assertEqual(result, "Book removed successfully.")
        self.repo.remove.assert_called_once_with("1")

    def test_get_all_books(self):
        self.repo.get_all.return_value = ["Book1", "Book2"]
        result = self.service.get_all()
        self.assertEqual(result, ["Book1", "Book2"])

    def test_update_book_success(self):
        self.repo.update_book = MagicMock()
        result = self.service.update({"title": "New Title"}, "1")
        self.assertEqual(result, "Book updated successfully.")
        self.repo.update_book.assert_called_once_with("1", {"title": "New Title"})


class TestClientService(unittest.TestCase):

    def setUp(self):
        self.repo = MagicMock()
        self.service = ClientService(self.repo)

    def test_add_client_success(self):
        self.repo.add = MagicMock()
        result = self.service.add_client("1", "Client A")
        self.assertEqual(result, "Client added successfully.")
        self.repo.add.assert_called_once()

    def test_add_client_duplicate_id(self):
        self.repo.add.side_effect = DuplicateIDError("A validation error occurred")
        result = self.service.add_client("1", "Client A")
        self.assertEqual(result, "Error: Client with ID 1 already exists.")

    def test_remove_client_success(self):
        self.repo.remove = MagicMock()
        result = self.service.remove_client("1", [],self.repo)
        self.assertEqual(result, "Client removed successfully.")
        self.repo.remove.assert_called_once_with("1")

    def test_get_all_clients(self):
        self.repo.get_all.return_value = ["Client1", "Client2"]
        result = self.service.get_all()
        self.assertEqual(result, ["Client1", "Client2"])

    def test_update_client_success(self):
        self.repo.update_client = MagicMock()
        result = self.service.update({"name": "New Client Name"}, "1")
        self.assertEqual(result, "Client updated successfully.")
        self.repo.update_client.assert_called_once_with("1", {"name": "New Client Name"})

if __name__ == '__main__':
    def run_tests():
        unittest.main()