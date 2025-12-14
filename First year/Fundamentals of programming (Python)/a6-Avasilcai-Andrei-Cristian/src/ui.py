#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
import copy
from texttable import Texttable
from functions import add_contestant, insert_contestant, remove_contestant, replace_contestant, list_contestant, top_contestant, undo_contestant


def print_list(contestants: list):
    if len(contestants)>0:
        t = Texttable()
        headers = list(contestants[0].keys())
        t.header(headers)
        for row in contestants:
            t.add_row([row[key] for key in headers])
        print(t.draw())
    else:
        print("Nothing to print!")


def run_ui():
    command_list = {
        "add": add_contestant,
        "insert": insert_contestant,
        "remove": remove_contestant,
        "replace": replace_contestant,
        "list": list_contestant,
        "top": top_contestant,
        "undo": undo_contestant,
        "print": print_list
    }
    contestants = [
        {"p1": 2, "p2": 9, "p3": 7},
        {"p1": 8, "p2": 1, "p3": 6},
        {"p1": 4, "p2": 10, "p3": 3},
        {"p1": 6, "p2": 3, "p3": 9},
        {"p1": 5, "p2": 7, "p3": 0},
        {"p1": 10, "p2": 2, "p3": 8},
        {"p1": 1, "p2": 5, "p3": 10},
        {"p1": 10, "p2": 10, "p3": 10},
        {"p1": 3, "p2": 8, "p3": 2},
        {"p1": 9, "p2": 6, "p3": 1}
    ]
    history = []

    while True:
        command = input(">").strip().lower()
        if command == "exit":
            break

        if len(command) > 0:
            com = command.split()[0]
            if com in command_list:
                try:
                    if com == "undo":
                        if history:
                            contestants = undo_contestant(history)
                            print("Undo successful.")
                        else:
                            print("Nothing to undo!")
                    elif com == "list" or com =="top":
                        if command == "list":
                            print_list(contestants)
                        else:
                            display_list = command_list[com](command, contestants)
                            if display_list:
                                print_list(display_list)
                            else:
                                print("No contestants matching criteria.")
                    else:
                        if com in {"add", "insert", "remove", "replace"}:
                            history.append(copy.deepcopy(contestants))
                        command_list[com](command, contestants)
                except ValueError as ve:
                    print(f"Error: {ve}")
                    if com in {"add", "insert", "remove", "replace"} and history:
                        history.pop()
            else:
                print("Unknown command! Please try again.")
        else:
            print("Empty command! Please enter a valid command.")
