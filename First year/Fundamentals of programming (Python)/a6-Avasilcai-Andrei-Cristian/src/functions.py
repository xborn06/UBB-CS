#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#


def create_contestant(n1: int, n2: int, n3: int):
    '''
    function that creates a dict containing a contestant's scores
    :param n1:
    :param n2:
    :param n3:
    :return: the dictionary created
    '''
    return {
        "p1": n1,
        "p2": n2,
        "p3": n3
    }


def get_score(contestant: dict, nr: int):
    if nr < 1 or nr > 3:
        raise ValueError("Invalid grade field!")
    p = "p" + str(nr)
    return contestant[p]


def set_scores(contestant: dict, nr: int, score: int):
    if score < 0 or score > 10:
        raise ValueError("Invalid score!")
    p = "p" + str(nr)
    contestant[p] = score


def add_contestant(command: str, contestants: list):
    '''
    function that adds to the contestants list a contestant with his/hers scores
    :param command:
    :param contestants:
    :return: nothing, just adds the dict to the list
    '''
    elems = command.split()
    if len(elems) != 4:
        raise ValueError("Invalid command!")
    try:
        n1 = int(elems[1])
        n2 = int(elems[2])
        n3 = int(elems[3])
        if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
            raise ValueError("Invalid grades!")
    except ValueError:
        raise ValueError("Invalid grades!")
    contestants.append(create_contestant(n1, n2, n3))


def insert_contestant(command: str, contestants: list):
    '''
    function that inserts a contestant at a certain given position
    :param command:
    :param contestants:
    :return: nothing, just inserts the dict in position given by the user
    '''
    elems = command.split()
    if len(elems) != 6:
        raise ValueError("Invalid command!")
    try:
        n1 = int(elems[1])
        n2 = int(elems[2])
        n3 = int(elems[3])
        if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
            raise ValueError("Invalid grades!")
    except ValueError:
        raise ValueError("Invalid grades!")
    try:
        pos = int(elems[5])
        pos -= 1
        if pos >= len(contestants) or pos < 0:
            raise ValueError("Invalid position!")
    except ValueError:
        raise ValueError("Invalid position!")
    contestants.append(
        create_contestant(contestants[-1]["p1"], contestants[-1]["p2"], contestants[-1]["p3"]))
    for i in range(len(contestants) - 2, pos, -1):
        set_scores(contestants[i], 1, get_score(contestants[i - 1], 1))
        set_scores(contestants[i], 2, get_score(contestants[i - 1], 2))
        set_scores(contestants[i], 3, get_score(contestants[i - 1], 3))
    set_scores(contestants[pos], 1, n1)
    set_scores(contestants[pos], 2, n2)
    set_scores(contestants[pos], 3, n3)


def remove1(elems: list, contestants: list):
    '''
    function that "removes" a contestant (it just sets all his scores to 0)
    :param elems:
    :param contestants:
    :return: nothing, just sets the scores of a dict
    '''
    try:
        pos = int(elems[1])
        pos -= 1
        if pos < 0 or pos >= len(contestants):
            raise ValueError("Invalid position!")
    except ValueError:
        raise ValueError("Invalid position!")
    del contestants[pos]


def remove2(elems: list, contestants: list):
    '''
    function that "removes" (sets all 3 scores to 0) contestants from the list based on a given criteria (it's average score is lower/equal/bigger than/to a given score)
    :param elems:
    :param contestants:
    :return: nothing, just modifies the contestants list
    '''
    try:
        score = int(elems[2])
        if score < 0 or score > 10:
            raise ValueError("Invalid score")
    except ValueError:
        raise ValueError("Invalid command!")
    if elems[1] == '=':
        contestants[:] = [c for c in contestants if (get_score(c, 1) + get_score(c, 2) + get_score(c, 3)) / 3 != score]
    elif elems[1] == '<':
        contestants[:] = [c for c in contestants if (get_score(c, 1) + get_score(c, 2) + get_score(c, 3)) / 3 > score]
    elif elems[1] == '>':
        contestants[:] = [c for c in contestants if (get_score(c, 1) + get_score(c, 2) + get_score(c, 3)) / 3 < score]
    else:
        raise ValueError("Invalid command!")


def remove3(elems: list, contestants: list):
    '''
    function that "removes" (sets all 3 scores to 0) contestants between 2 given positions (including the positions themselves)
    :param elems:
    :param contestants:
    :return: nothing, just modifies the contestants list
    '''
    try:
        p1 = int(elems[1])
        p2 = int(elems[3])
        p1 -= 1
        p2 -= 1
        if p1 < 0 or p1 >= len(contestants) or p2 < 0 or p2 >= len(contestants):
            raise ValueError("Invalid positions!")
    except ValueError:
        raise ValueError("Invalid positions!")
    del contestants[p1:p2 + 1]


def remove_contestant(command: str, contestants: list):
    '''
    function that interprets the command given by the user, and it calls the corresponding function for the user's intention
    :param command:
    :param contestants:
    :return: nothing, just calls one function each time depending on the user input
    '''
    elems = command.split()
    if len(elems) != 2 and len(elems) != 3 and len(elems) != 4:
        raise ValueError("Invalid command!")
    if len(elems) == 2:
        remove1(elems, contestants)
    elif len(elems) == 3:
        remove2(elems, contestants)
    elif len(elems) == 4:
        remove3(elems, contestants)


def replace_contestant(command: str, contestants: list):
    '''
    function that modifies one of the 3 scores of a contestant
    :param command:
    :param contestants:
    :return: nothing, just sets the new value to the corresponding grade field given by the user
    '''
    elems = command.split()
    if len(elems) != 5:
        raise ValueError("Invalid command!")
    try:
        pos = int(elems[1])
        pos -= 1
        if pos < 0 or pos >= len(contestants):
            raise ValueError("Invalid position!")
    except ValueError:
        raise ValueError("Invalid position!")
    try:
        grade_field = int(elems[2][1])
        if grade_field < 1 or grade_field > 3:
            raise ValueError("Invalid grade field!")
    except ValueError:
        raise ValueError("Invalid grade field!")
    try:
        new_score = int(elems[4])
    except ValueError:
        raise ValueError("Invalid new score!")
    set_scores(contestants[pos], grade_field, new_score)


def sort_list(contestants: list):
    '''
    function that sorts a dict list descending based on the average of the 3 scores
    :param contestants:
    :return: a sorted list
    '''
    return sorted(contestants, key=lambda x: (get_score(x, 1) + get_score(x, 2) + get_score(x, 3)) / 3, reverse=True)


def list1(contestants: list):
    '''
    function that puts in another list a sorted version of the contestants list and returns it to the ui for printing"
    :param contestants:
    :return: the sorted list
    '''
    contestants1 = sort_list(contestants)
    return contestants1


def list2(elems: list, contestants: list):
    '''
    function that returns the contestants list filtered by some criteria given by the user
    :param elems:
    :param contestants:
    :return: filtered list
    '''
    display_list = []
    if elems[1] == '<':
        try:
            score = int(elems[2])
            if score < 0 or score > 10:
                raise ValueError("Invalid score!")
        except ValueError:
            raise ValueError("Invalid score!")
        for i in contestants:
            if int((get_score(i, 1) + get_score(i, 2) + get_score(i, 3)) / 3) < score:
                display_list.append(i)
        if len(display_list) > 0:
            return display_list
    elif elems[1] == '=':
        try:
            score = int(elems[2])
            if score < 0 or score > 10:
                raise ValueError("Invalid score!")
        except ValueError:
            raise ValueError("Invalid score!")
        for i in contestants:
            if int((get_score(i, 1) + get_score(i, 2) + get_score(i, 3)) / 3) == score:
                display_list.append(i)
        if len(display_list) > 0:
            return display_list
    elif elems[1] == '>':
        try:
            score = int(elems[2])
            if score < 0 or score > 10:
                raise ValueError("Invalid score!")
        except ValueError:
            raise ValueError("Invalid score!")
        for i in contestants:
            if int((get_score(i, 1) + get_score(i, 2) + get_score(i, 3)) / 3) > score:
                display_list.append(i)
        if len(display_list) > 0:
            return display_list
    else:
        raise ValueError("Invalid command!")


def list_contestant(command: str, contestants: list):
    '''
    function that interprets the user's input and calls the right function depending on his/hers intent
    :param command:
    :param contestants:
    :return: nothing, just calls certain functions
    '''
    if command == "list sorted":
        return list1(contestants)
    elems = command.split()
    if len(elems) == 3:
        return list2(elems, contestants)
    else:
        raise ValueError("Invalid command!")


def list_sort_by_field(contestant: list, field: int):
    '''
    function that sorts a dict list depending on a certain grade field
    :param contestant:
    :param field:
    :return: the sorted list by a grade field
    '''
    if field < 1 or field > 3:
        raise ValueError("Invalid grade field!")
    grade = "p" + str(field)
    return sorted(contestant, key=lambda x: x[grade], reverse=True)


def top1(contestants: list, elems: list):
    '''
    functiop that displays the top x contestants
    :param contestants:
    :param elems:
    :return: nothing, just displays a list of contestants
    '''
    try:
        nr = int(elems[1])
        if nr <= 0 or nr > len(contestants):
            raise ValueError("Invalid number of contestants!")
    except ValueError:
        raise ValueError("Invalid number of contestants!")
    display_list = []
    contestants = sort_list(contestants)
    for i in range(0, nr):
        display_list.append(contestants[i])
    return display_list


def top2(contestants: list, elems: list):
    '''
    function that displays a list of top x contestants based on a grade field
    :param contestants:
    :param elems:
    :return: nothing, just displays a list
    '''
    display_list = []
    try:
        nr = int(elems[1])
        if nr <= 0 or nr > len(contestants):
            raise ValueError("Invalid number of contestants!")
    except ValueError:
        raise ValueError("Invalid number of contestants!")
    try:
        grade_field = int(elems[2][1])
        if grade_field < 1 or grade_field > 3:
            raise ValueError("Invalid grade field!")
    except ValueError:
        raise ValueError("Invalid grade field!")
    contestants = list_sort_by_field(contestants, grade_field)
    for i in range(0, nr):
        display_list.append(contestants[i])
    return display_list


def top_contestant(command: str, contestants: list):
    '''
    function that interprets the user's input and calls the required function
    :param command:
    :param contestants:
    :return: nothing, just calls specific functions
    '''
    elems = command.split()
    if len(elems) == 2:
        return top1(contestants, elems)
    elif len(elems) == 3:
        return top2(contestants, elems)
    else:
        raise ValueError("Invalid command!")


def undo_contestant(h: list):
    '''
    function that gives the contestants list before it suffered its last alternation
    :param h:
    :return: a previous contestants list
    '''
    return h.pop()
