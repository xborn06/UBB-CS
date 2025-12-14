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

class IDValidatorException(KeyError):
    def __init__(self, message="A validation error occurred"):
        super().__init__(message)
        self.message = message

class ValidationException(Exception):
    def __init__(self, message = "A validation error occurred"):
        super().__init__(message)
        self.message = message


class UI:
    def __init__(self, book_service, client_service, rental_service):
        self._book_service = book_service
        self._client_service = client_service
        self._rental_service = rental_service


    def printMainMenu(self):
        print("1.Manage clients and books")
        print("2.Rent or return a book")
        print("3.Search")
        print("4.List rentals")
        print("5.Undo")
        print("6.Redo")
        print("7.Most rented books")
        print("8.Most active clients")
        print("9.Most rented authors")
        print("10.Exit")

    def printMenu1(self):
        print("1.Clients")
        print("2.Books")
        x = input("")
        return x

    def printMenu2(self):
        print("1.Rent")
        print("2.Return")
        x = input("")
        return x

    def printMenuFieldBooks(self):
        print("1.Id")
        print("2.Title")
        print("3.Author")
        x = input("")
        return x

    def printMenuFieldClients(self):
        print("1.Id")
        print("2.Name")
        x = input("")
        return x

    def printGeneralMenu(self):
        print("1.Add")
        print("2.Remove")
        print("3.Update")
        print("4.List")

    def display_books(self):
        books = self._book_service.get_all()
        if books:
            print("Books in the repository:")
            for book in books:
                print(book)
        else:
             print("No books in the repository.")

    def display_clients(self):
        clients = self._client_service.get_all()
        if clients:
            print("Clients in the repository:")
            for client in clients:
                print(client)
        else:
            print("No clients in the repository.")

    def display_rentals(self):
        rentals = self._rental_service.get_all()
        if rentals:
            print("Rentals in the repository:")
            for rental in rentals:
                print(rental)
        else:
            print("No rentals in the repository.")

    def run(self):
        last_used_service = 0
        last_stack = []
        redo_stack = []
        while True:
            self.printMainMenu()
            choice = input("Choose an option: ")

            if choice == '1':
                c = self.printMenu1()
                if c == '2':
                    self.printGeneralMenu()
                    c1 = input("Choose an option: ")
                    if c1 == '1':
                        id = input("Insert id: ")
                        title = input("Insert title: ")
                        author = input("Insert author: ")
                        try:
                            print(self._book_service.add_book(id,author,title))
                            last_stack.append(1)
                        except ValidationException as ve:
                            print(ve)
                    elif c1 == '2':
                        id = input("Insert id:")
                        try:
                            print(self._book_service.remove_book(id,self._rental_service.repo.get_all(),self._rental_service.repo))
                            last_stack.append(1)
                        except IDNotFoundError as idnfe:
                            print(idnfe)
                    elif c1 == '3':
                        id = input("Insert id: ")
                        title = input("Insert new title: ")
                        author = input("Insert new author: ")
                        d = {
                            'title' : title,
                            'author' : author
                        }
                        try:
                            print(self._book_service.update(d,id))
                            last_stack.append(1)
                        except IDNotFoundError as idnfe:
                            print(idnfe)
                        except ValidationException as ve:
                            print(ve)
                    elif c1 == '4':
                        self.display_books()
                    else:
                        print("Invalid option!")
                elif c == '1':
                    self.printGeneralMenu()
                    c1 = input("Choose an option: ")
                    if c1 == '1':
                        id = input("Insert id: ")
                        name = input("Insert name: ")
                        try:
                            print(self._client_service.add_client(id,name))
                            last_stack.append(2)
                        except ValidationException as ve:
                            print(ve)
                    elif c1 == '2':
                        id = input("Insert id: ")
                        try:
                            print(self._client_service.remove_client(id,self._rental_service.repo.get_all(),self._rental_service.repo))
                            last_stack.append(2)
                        except IDNotFoundError as idnfe:
                            print(idnfe)
                    elif c1 == '3':
                        id = input("Insert id: ")
                        name = input("Insert new name: ")
                        d = {
                            'name' : name
                        }
                        try:
                            print(self._client_service.update(d,id))
                            last_stack.append(2)
                        except IDNotFoundError as idnfe:
                            print(idnfe)
                        except ValidationException as ve:
                            print(ve)
                    elif c1 == '4':
                        self.display_clients()
                    else:
                        print("Invalid option!")
            elif choice == '2':
                c = self.printMenu2()
                if c == '1':
                    if len(self._rental_service.repo) > 0:
                        last_id = self._rental_service.repo.get_last_rental_id()
                        numeric_part = int(last_id[1:])
                        new_id_numeric = numeric_part + 1
                        id = f"R{new_id_numeric:03}"
                    else:
                        id = "R001"
                    bid = input("Insert book id: ")
                    cid = input("Insert client id: ")
                    date1 = input("Insert rent date(dd/mm/yyyy): ")
                    date2 = input("Insert return date(dd/mm/yyyy): ")
                    try:
                        print(self._rental_service.add_rental(id,bid,cid,date1,date2,self._book_service.get_all(),self._client_service.get_all()))
                        last_stack.append(3)
                    except ValidationException as ve:
                        print(ve)
                elif c == '2':
                    id = input("Insert rental id: ")
                    try:
                        print(self._rental_service.remove_rental(id))
                        last_stack.append(3)
                    except IDNotFoundError as idnfe:
                        print(idnfe)
                    except IDValidatorException as idv:
                        print(idv)
                else:
                    print("Invalid option!")
            elif choice == '3':
                c = self.printMenu1()
                if c == '1':
                    c1 = self.printMenuFieldClients()
                    if c1 == '1':
                        id = input("Insert id: ")
                        print(self._client_service.find(1,id))
                    elif c1 == '2':
                        name = input("Insert name: ")
                        print(self._client_service.find(2,name))
                    else:
                        print("Invalid option!")
                elif c == '2':
                    c1 = self.printMenuFieldBooks()
                    if c1 == '1':
                        id = input("Insert id: ")
                        print(self._book_service.find(1,id))
                    elif c1 == '2':
                        title = input("Insert title: ")
                        print(self._book_service.find(2,title))
                    elif c1 == '3':
                        author = input("Insert author: ")
                        print(self._book_service.find(3,author))
                    else:
                        print("Invalid option!")
                else:
                    print("Invalid option!")
            elif choice == '4':
                self.display_rentals()
            elif choice == '5':
                last_used_service = last_stack.pop() if len(last_stack) > 0 else 0
                if last_used_service == 0:
                    print("Nothing to undo!")
                elif last_used_service == 1:
                    try:
                        self._book_service.undo_action()
                        redo_stack.append(1)
                    except Exception as e:
                        print(e)
                elif last_used_service == 2:
                    try:
                        self._client_service.undo_action()
                        redo_stack.append(2)
                    except Exception as e:
                        print(e)
                elif last_used_service == 3:
                    try:
                        self._rental_service.undo_action()
                        redo_stack.append(3)
                    except Exception as e:
                        print(e)
            elif choice == '6':
                last_used_service = redo_stack.pop() if len(redo_stack) > 0 else 0
                if last_used_service == 0:
                    print("Nothing to redo!")
                elif last_used_service == 1:
                    try:
                        self._book_service.redo_action()
                        last_stack.append(1)
                    except Exception as e:
                        print(e)
                elif last_used_service == 2:
                    try:
                        self._client_service.redo_action()
                        last_stack.append(2)
                    except Exception as e:
                        print(e)
                elif last_used_service == 3:
                    try:
                        self._rental_service.redo_action()
                        last_stack.append(3)
                    except Exception as e:
                        print(e)
            elif choice == '7':
                for element in self._rental_service.get_most_rented_books(self._book_service._repo):
                    print(element)
            elif choice == '8':
                for element in self._rental_service.get_most_active_clients():
                    print(element)
            elif choice == '9':
                for element in self._rental_service.get_most_rented_authors(self._book_service._repo):
                    print(element)
            elif choice == '10':
                break
            else:
                print("Invalid option!")


