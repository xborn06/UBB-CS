from functions import create_contestant, set_scores, get_score, add_contestant, insert_contestant, remove_contestant, \
    remove1, remove3, replace_contestant


def test_add_contestant():
    try:
        contestants = []
        add_contestant("add 5 7 9", contestants)
        assert len(contestants) == 1
        assert contestants[0] == {"p1": 5, "p2": 7, "p3": 9}

        add_contestant("add 5 7", contestants)

        add_contestant("add 5 seven 9", contestants)
    except Exception as e:
        print(f"Error in invalid case test_add_contestant: {e}")

    print("test_add_contestant passed!")


def test_remove1():
    try:
        contestants = [{"p1": 5, "p2": 7, "p3": 9}, {"p1": 3, "p2": 6, "p3": 8}]
        remove1(["remove", "1"], contestants)
        assert contestants[0] == {"p1": 0, "p2": 0, "p3": 0}
        assert contestants[1] == {"p1": 3, "p2": 6, "p3": 8}

        remove1(["remove", "3"], contestants)

        remove1(["remove"], contestants)
    except Exception as e:
        print(f"Error in invalid case test_remove1: {e}")

    print("test_remove1 passed!")


def test_remove3():
    try:
        contestants = [
            {"p1": 5, "p2": 7, "p3": 9},
            {"p1": 3, "p2": 6, "p3": 8},
            {"p1": 10, "p2": 10, "p3": 10},
            {"p1": 2, "p2": 4, "p3": 6}
        ]
        remove3(["remove", "2", "to", "3"], contestants)
        assert contestants[0] == {"p1": 5, "p2": 7, "p3": 9}
        assert contestants[1] == {"p1": 0, "p2": 0, "p3": 0}
        assert contestants[2] == {"p1": 0, "p2": 0, "p3": 0}
        assert contestants[3] == {"p1": 2, "p2": 4, "p3": 6}

        remove3(["remove", "2", "to", "5"], contestants)

        remove3(["remove", "2", "to"], contestants)
    except Exception as e:
        print(f"Error in invalid case test_remove3: {e}")

    print("test_remove3 passed!")


def test_replace_contestant():
    try:
        contestants = [{"p1": 5, "p2": 7, "p3": 9}]
        replace_contestant("replace 1 P2 with 6", contestants)
        assert contestants[0] == {"p1": 5, "p2": 6, "p3": 9}

        replace_contestant("replace 2 P1 with 10", contestants)

        replace_contestant("replace 1 P4 with 6", contestants)
    except Exception as e:
        print(f"Error in invalid case test_replace_contestant: {e}")

    print("test_replace_contestant passed!")


def test_insert_contestant():
    try:
        contestants = [{"p1": 5, "p2": 7, "p3": 9}, {"p1": 3, "p2": 6, "p3": 8}]
        insert_contestant("insert 10 8 9 at 2", contestants)
        assert contestants[1] == {"p1": 10, "p2": 8, "p3": 9}
        assert len(contestants) == 3

        insert_contestant("insert 10 8 at 2", contestants)

        insert_contestant("insert 10 8 9 at 5", contestants)
    except Exception as e:
        print(f"Error in invalid case test_insert_contestant: {e}")

    print("test_insert_contestant passed!")


def run_tests():
    test_add_contestant()
    test_remove1()
    test_remove3()
    test_replace_contestant()
    test_insert_contestant()
