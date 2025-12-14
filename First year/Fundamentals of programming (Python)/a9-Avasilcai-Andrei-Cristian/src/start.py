from datetime import timedelta
from src.repository.binary_repo import ClientBinaryRepository, BookBinaryRepository, RentalBinaryRepository
from src.repository.text_repo import BookFileRepository, ClientFileRepository, RentalFileRepository
from src.repository.memoery_repo import BookMemoryRepository, ClientMemoryRepository, RentalMemoryRepository
from src.services.rental_service import RentalService
from src.services.client_service import ClientService
from src.services.book_service import BookService
from src.ui.ui import UI
from faker import Faker
import random
from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental

class SimpleConfigLoader:
    def __init__(self, config_file_path):
        self.config = self._load_config(config_file_path)

    def _load_config(self, file_path):
        config = {}
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.split('#', 1)[0].strip()
                if line:
                    key, value = line.split('=', 1)
                    value = value.strip().strip('"')
                    config[key.strip()] = value
        return config

    def get(self, key, default=None):
        return self.config.get(key, default)



def initialize_repositories(config_file_path):
    config_loader = SimpleConfigLoader(config_file_path)
    repository_type = config_loader.get('repository')
    if repository_type != 'inmemory':
        books_file = config_loader.get('books')
        clients_file = config_loader.get('clients')
        rentals_file = config_loader.get('rentals')
        if not books_file or not clients_file or not rentals_file:
            raise ValueError("File paths not properly configured in settings.properties")



    if repository_type == 'inmemory':
        books_repo = BookMemoryRepository()
        clients_repo = ClientMemoryRepository()
        rentals_repo = RentalMemoryRepository()
    elif repository_type == 'textfiles':
        books_repo = BookFileRepository(books_file)
        clients_repo = ClientFileRepository(clients_file)
        rentals_repo = RentalFileRepository(rentals_file)
    elif repository_type == 'binaryfiles':
        books_repo = BookBinaryRepository(books_file)
        clients_repo = ClientBinaryRepository(clients_file)
        rentals_repo = RentalBinaryRepository(rentals_file)
    else:
        raise ValueError(f"Unknown repository type: {repository_type}")

    return books_repo, clients_repo, rentals_repo




fake = Faker()


def generate_books(num_books=20):
    books = []
    for i in range(1, num_books + 1):
        author = fake.name()
        title = fake.catch_phrase()
        book_id = f"B{i:03}"
        books.append(Book(book_id, author, title))
    return books


def generate_clients(num_clients=20):
    clients = []
    for i in range(1, num_clients + 1):
        client_id = f"C{i:03}"
        name = fake.name()
        clients.append(Client(client_id, name))
    return clients


def generate_rentals(count, books, clients):
    rentals = []
    for i in range(1, count + 1):
        rental_id = f"R{i:03}"
        book = random.choice(books)
        client = random.choice(clients)
        start_date = fake.date_between(start_date='-1y', end_date='today')
        end_date = fake.date_between(start_date=start_date, end_date=start_date + timedelta(days=30))

        rentals.append(Rental(
            id=rental_id,
            book_id=book.id,
            client_id=client.id,
            rented_date=start_date,
            return_date=end_date
        ))
    return rentals


def main():
    books_repo, clients_repo, rentals_repo = initialize_repositories('settings.properties')
    books = generate_books(20)
    clients = generate_clients(20)
    rentals = generate_rentals(20, books, clients)
    if len(books_repo) == 0:
        for book in books:
            books_repo.add(book)
    if len(clients_repo) == 0:
        for client in clients:
            clients_repo.add(client)
    if len(rentals_repo) == 0:
        for rental in rentals:
            rentals_repo.add(rental)
    bookservice = BookService(books_repo)
    clientservice = ClientService(clients_repo)
    rentalservice = RentalService(rentals_repo)
    ui = UI(bookservice, clientservice, rentalservice)
    ui.run()


if __name__ == "__main__":
    main()
