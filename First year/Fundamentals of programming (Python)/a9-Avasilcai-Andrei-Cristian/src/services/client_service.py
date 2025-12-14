from src.domain.client import Client
from src.repository.memoery_repo import IDNotFoundError
from src.repository.memoery_repo import DuplicateIDError,NameNotFoundError

class IDValidatorException(KeyError):
    def __init__(self, message="A validation error occurred"):
        super().__init__(message)
        self.message = message

class ValidationException(Exception):
    def __init__(self, message = "A validation error occurred"):
        super().__init__(message)
        self.message = message

class ClientService:
    def __init__(self, repo):
        """
        The repo parameter is the repository passed from outside (e.g., MemoryRepository)
        :param repo: Repository-like object that implements the necessary methods
        """
        self._repo = repo
        self._undo_stack = []
        self._redo_stack = []

    def add_client(self, id: str, name: str):
        """
        Adds a client to the repository. Returns a success or error message.
        :param id: the unique identifier
        :param name: the name of the client
        :return: success or error message
        """
        client = Client(id, name)
        try:
            self._repo.add(client)
            self._undo_stack.append(("remove", id, name))
            self._redo_stack.clear()
            return "Client added successfully."
        except DuplicateIDError:
            return f"Error: Client with ID {id} already exists."
        except ValidationException as e:
            return f"Error: {str(e)}"

    def add_client_undo(self, id: str, name: str):
        """
        Adds a client to the repository. Returns a success or error message.
        :param id: the unique identifier
        :param name: the name of the client
        :return: success or error message
        """
        client = Client(id, name)
        try:
            self._repo.add(client)
            return "Client added successfully."
        except DuplicateIDError:
            return f"Error: Client with ID {id} already exists."
        except ValidationException as e:
            return f"Error: {str(e)}"

    def add_client_redo(self, id: str, name: str):
        """
        Adds a client to the repository. Returns a success or error message.
        :param id: the unique identifier
        :param name: the name of the client
        :return: success or error message
        """
        client = Client(id, name)
        try:
            self._repo.add(client)
            self._undo_stack.append(("remove", id, name))
            return "Client added successfully."
        except DuplicateIDError:
            return f"Error: Client with ID {id} already exists."
        except ValidationException as e:
            return f"Error: {str(e)}"


    def remove_client(self, id: str, rental_list: list, rental_repo):
        """
        Remove a client from the collection based on its unique identifier.
        :param id: Unique identifier for the client that needs to be removed.
        :return:
        """
        try:
            client_to_remove = self._repo[id]
            if not client_to_remove:
                raise IDNotFoundError(f"No client found with ID: {id}")
            if rental_list:
                associated_rentals = [rental for rental in rental_list if rental.client_id == id]
            else:
                associated_rentals = []
            self._undo_stack.append(("add", id, client_to_remove, associated_rentals, rental_repo))
            for rental in rental_list:
                if rental.client_id == id:
                    rental_repo.remove(rental.id)
            self._repo.remove(id)
            self._redo_stack.clear()
            return "Client removed successfully."
        except IDNotFoundError:
            return f"Error: Client with ID {id} not found"

    def remove_client_undo(self, id: str, rental_list: list, rental_repo):
        """
        Remove a client from the collection based on its unique identifier.
        :param id: Unique identifier for the client that needs to be removed.
        :return:
        """
        try:
            client_to_remove = self._repo[id]
            if not client_to_remove:
                raise IDNotFoundError(f"No client found with ID: {id}")
            for rental in rental_list:
                if rental.client_id == id:
                    rental_repo.remove(rental.id)
            self._repo.remove(id)
            return "Client removed successfully."
        except IDNotFoundError:
            return f"Error: Client with ID {id} not found"

    def remove_client_redo(self, id: str, rental_list: list, rental_repo):
        """
        Remove a client from the collection based on its unique identifier.
        :param id: Unique identifier for the client that needs to be removed.
        :return:
        """
        try:
            client_to_remove = self._repo[id]
            if not client_to_remove:
                raise IDNotFoundError(f"No client found with ID: {id}")
            if rental_list:
                associated_rentals = [rental for rental in rental_list if rental.client_id == id]
            else:
                associated_rentals = []
            self._undo_stack.append(("add", id, client_to_remove, associated_rentals, rental_repo))
            for rental in rental_list:
                if rental.client_id == id:
                    rental_repo.remove(rental.id)
            self._repo.remove(id)
            return "Client removed successfully."
        except IDNotFoundError:
            return f"Error: Client with ID {id} not found"

    def get_all(self) -> list:
        """
        Returns a list with all the clients in the repository.
        :return: list of all clients
        """
        return self._repo.get_all()

    def find(self,find_type: int, user_input: str):
        """
        Searches for a client in the repo based on id/name
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
                return self._repo.find_by_name(user_input)
            except NameNotFoundError as ve:
                return f"Error: {str(ve)}"

    def update(self, new_data, id):
        """
        Updates a client's information (name)
        :param new_data:
        :param id:
        :return:
        """
        try:
            client_to_update = self._repo._data[id]
            original_data = {
                "name": client_to_update.name
            }
            self._undo_stack.append(("update", id, original_data))
            self._repo.update_client(id, new_data)
            self._redo_stack.clear()
            return "Client updated successfully."
        except IDNotFoundError as idnfe:
            return f"Error: {str(idnfe)}"
        except ValidationException as ve:
            return f"Error: {str(ve)}"

    def update_undo(self, new_data, id):
        """
        Updates a client's information (name)
        :param new_data:
        :param id:
        :return:
        """
        try:
            self._repo.update_client(id, new_data)
            return "Client updated successfully."
        except IDNotFoundError as idnfe:
            return f"Error: {str(idnfe)}"
        except ValidationException as ve:
            return f"Error: {str(ve)}"

    def update_redo(self, new_data, id):
        """
        Updates a client's information (name)
        :param new_data:
        :param id:
        :return:
        """
        try:
            client_to_update = self._repo._data[id]
            original_data = {
                "name": client_to_update.name
            }
            self._undo_stack.append(("update", id, original_data))
            self._repo.update_client(id, new_data)
            return "Client updated successfully."
        except IDNotFoundError as idnfe:
            return f"Error: {str(idnfe)}"
        except ValidationException as ve:
            return f"Error: {str(ve)}"

    def undo_action(self):
        if not self._undo_stack:
            raise Exception("No actions to undo!")
        action = self._undo_stack.pop()
        if action[0] == "add":
            client_id, client, related_rentals, rental_repo = action[1], action[2], action[3], action[4]
            self.add_client_undo(client_id, client.name)
            for rental in related_rentals:
                rental_repo.add(rental)
            self._redo_stack.append(("remove", client_id, related_rentals, rental_repo))
        elif action[0] == "remove":
            client_id = action[1]
            client_name = action[2]
            self.remove_client_undo(client_id, [], [])
            self._redo_stack.append(("add", client_id, client_name))
        elif action[0] == "update":
            client_id, original_data = action[1], action[2]
            new_data = {
                'name': self._repo._data[client_id].name,
            }
            self.update_undo(original_data, client_id)
            self._redo_stack.append(("update", client_id, new_data))

    def redo_action(self):
        if not self._redo_stack:
            raise Exception("No actions to redo!")
        action = self._redo_stack.pop()
        if action[0] == "add":
            client_id, client_name = action[1], action[2]
            self.add_client_redo(client_id, client_name)
        elif action[0] == "remove":
            client_id = action[1]
            related_rentals = action[2]
            rental_repo = action[3]
            self.remove_client_redo(client_id, related_rentals, rental_repo)
        elif action[0] == "update":
            client_id, new_data = action[1], action[2]
            self.update_redo(new_data, client_id)
