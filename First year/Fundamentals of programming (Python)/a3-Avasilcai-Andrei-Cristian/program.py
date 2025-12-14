import random
import math
import timeit
import time


def list_merger(l1: list, l2: list) -> list:
    merged = []
    i = int(0)
    j = int(0)
    length1 = len(l1)
    length2 = len(l2)
    while i < length1 and j < length2:
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
    while i < length1:
        merged.append(l1[i])
        i += 1
    while j < length2:
        merged.append(l2[j])
        j += 1
    return merged


def strand_sort(l: list, steps: int) -> list:
    sorted_l = []
    steps_counter = int(0)
    while l:
        steps_counter += 1
        strand = [l[0]]
        l.pop(0)
        i = 0
        while i < len(l):
            if l[i] > strand[-1]:
                strand.append(l[i])
                l.pop(i)
            else:
                i += 1
        sorted_l = list_merger(sorted_l, strand)
        if steps_counter == steps:
            steps_counter = 0
            print("Sorted items so far: ", sorted_l, " and the remaining items: ", l)
    return sorted_l


def strand_sort_for_timing(l: list) -> list:
    sorted_l = []
    while l:
        strand = [l[0]]
        l.pop(0)
        i = 0
        while i < len(l):
            if l[i] > strand[-1]:
                strand.append(l[i])
                l.pop(i)
            else:
                i += 1
        sorted_l = list_merger(sorted_l, strand)
    return sorted_l


def selection_sort(l: list, steps: int) -> list:
    steps_counter = int(0)
    length = len(l)
    for i in range(length):
        steps_counter += 1
        min = i
        for j in range(i + 1, length):
            if l[j] < l[min]:
                min = j
        if min != i:
            aux = l[i]
            l[i] = l[min]
            l[min] = aux
        if steps_counter == steps:
            print(l)
            steps_counter = 0
    return l


def selection_sort_for_timing(l: list) -> list:
    length = len(l)
    for i in range(length):
        min = i
        for j in range(i + 1, length):
            if l[j] < l[min]:
                min = j
        if min != i:
            aux = l[i]
            l[i] = l[min]
            l[min] = aux
    return l


def jump_search(x: int, l: list) -> int:
    step = int(math.sqrt(len(l)))
    length = len(l)
    s1 = 0
    s2 = step
    while s2 < length and l[s2] < x:
        s1 = s2
        s2 += step
    s2 = min(s2, length)
    for i in range(s1, s2 + 1):
        if l[i] == x:
            return i
    return -1


n = int(0)
ok = int(0)
while n != 5:
    print("1.Generate a random list of numbers")
    print("2.Search for an element using jump sort")
    print("3.Sort the list using Selection sort")
    print("4.Sort the list using Strand sort")
    print("5.Exit")
    print("6.Best case for the algorithms")
    print("7.Average case for the algorithms")
    print("8.Worst case for the algorithms")
    n = int(input("What would you like to do?"))
    if n > 8:
        n = int(input("That isn't an available option. Please try again:"))
    if n == 5:
        print("The program has ended")
        break
    if n < 5:
        if n == 1:
            print("What should the length of the list be?")
            length = int(input())
            while length <= 0:
                length = int(input("Please insert a valid value"))
            l = [random.randrange(1, 1000) for i in range(length)]
            print(l)
            ok = 1
        if ok == 0:
            print("The list wasn't generated yet")
        else:
            if n == 2:
                if ok < 2:
                    print("The list must be sorted before searching for elements")
                else:
                    print(l)
                    print("What is the number you want to search?")
                    x = int(input())
                    pos = jump_search(x, l)
                    if pos != -1:
                        print(jump_search(x, l))
                    else:
                        print("The given number is not part of the list")
            if n == 3:
                print("What should the interval between the shown steps be?")
                steps = int(input())
                print("Initial list: ", l)
                print("Final list: ", selection_sort(l, steps))
                ok = 2
            if n == 4:
                print("What should the interval between the shown steps be?")
                steps = int(input())
                print("Initial list: ", l)
                print("Final list: ", strand_sort(l, steps))
                print(l)
                ok = 2
    if n == 6:
        length1 = int(input("What should the starting length be?"))
        while length1 <= 0:
            length1 = int(input("Please insert a valid value"))
        i = int(5)
        while i:
            list1 = [random.randrange(1, 1000) for i in range(length1)]
            list1.sort()
            selection_sort_time1 = timeit.timeit(
                stmt='selection_sort_for_timing(list1.copy())',
                setup='from __main__ import selection_sort_for_timing, list1',
                number=1
            )
            # For selection sort in the best case it has a time complexity of O(n^2) and it occurs when the list is already sorted ascending,
            # because it needs to go for every position of the list and check if the lowest element available for that position is
            # already there, meaning it performs n-1 comparisons for the first element, then n-2 for the second and so on,
            # therefore it amounts to n*(n-1)/2, but for actual time complexity it means O(n^2)
            print(
                f"In the best case Selection Sort sorted a list of {length1} elements in {selection_sort_time1:.4f} seconds")
            strand_sort_time1 = timeit.timeit(
                stmt='strand_sort_for_timing(list1.copy())',
                setup='from __main__ import strand_sort_for_timing, list1',
                number=1
            )
            # For strand sort in the best case it has a time complexity of O(n) and it occurs when the list is already sorted ascending,
            # because the algorithm only goes through the list once and puts in the strand all the elements in one go, without having to do
            # any other merges, hence the time complexity of O(n)
            print(
                f"In the best case Strand Sort sorted a list of {length1} elements in {strand_sort_time1:.4f} seconds")
            i -= 1
            length1 *= 2
            print()
    if n == 7:
        length2 = int(input("What should the starting length be?"))
        while length2 <= 0:
            length2 = int(input("Please insert a valid value"))
        i = int(5)
        while i:
            list2 = [random.randrange(1, 1000) for i in range(length2)]
            selection_sort_time2 = timeit.timeit(
                stmt='selection_sort_for_timing(list2.copy())',
                setup='from __main__ import selection_sort_for_timing, list2',
                number=1
            )
            # In the average case, selection sort the time complexity is still O(n^2), due to the fact it still has to do the same number
            # of comparisons for every position in the list (n-1 for the first, n-2 for the second, ... ) amounting to n*(n-1)/2 which
            # in terms of complexity means O(n^2)
            print(
                f"In the average case Selection Sort sorted a list of {length2} elements in {selection_sort_time2:.4f} seconds")
            strand_sort_time2 = timeit.timeit(
                stmt='strand_sort_for_timing(list2.copy())',
                setup='from __main__ import strand_sort_for_timing, list2',
                number=1
            )
            # In the average case, strand sort has a time complexity of O(n^2), due to the fact that the number of strands created depends
            # on the order of the elements and if each strand only has a few elements added to it that results to many merges, and because
            # each element has an equal chance of being small or larger than the last one inserted in the strand sort we can only assume
            # that for each step there will be n-k comparison with k going from 0 to n-1, amounting to n*(n-1)/2 or O(n^2)
            print(
                f"In the average case Strand Sort sorted a list of {length2} elements in {strand_sort_time2:.4f} seconds")
            print()
            i -= 1
            length2 *= 2
    if n == 8:
        length3 = int(input("What should the starting length be?"))
        while length3 <= 0:
            length3 = int(input("Please insert a valid value"))
        i = int(5)
        while i:
            list3 = [random.randrange(1, 1000) for i in range(length3)]
            list3.sort(reverse=True)
            selection_sort_time3 = timeit.timeit(
                stmt='selection_sort_for_timing(list3.copy())',
                setup='from __main__ import selection_sort_for_timing, list3',
                number=1
            )
            # Worst case for selection sort happens when the list is ordered in descending order, because the algorithm has to go through
            # n-k (-1) comparisons for each step where k is the position the algorithm is currently searching the correct element to put there
            # meaning for position k (k goes from 0 to n-1 or 1 to n depending on the indexing) it will compare the element from the k-th
            # position to the ones that come after it, because those weren't sorted yet, and it will find it on the n-k (-1) -th position
            # (so for the first one the correct number will be on the n-1 -th position, for the second one it will be on the n-2 -th position, ...)

            # The complexity for selection sort remains the same across all cases, because its purpose is to compare all elements that come after
            # the current element to see if there is a lower one, no matter the original order of the list.
            print(
                f"In the worst case Selection Sort sorted a list of {length3} elements in {selection_sort_time3:.4f} seconds")
            strand_sort_time3 = timeit.timeit(
                stmt='strand_sort_for_timing(list3.copy())',
                setup='from __main__ import strand_sort_for_timing, list3',
                number=1
            )
            # Worst case for strand sort happens when the list is sorted in descending order, because each strand will contain only one element,
            # amounting to n strands which create a time complexity of O(n^2), because the algorithm will compare the element from the strand to
            # each remaining element in the original list (the first one will be compared to the rest of n-1, the second one with the rest of
            # n-2 and so on) leading to n*(n-1)/2 comparisons, although in the mergers themselves the element from the strand will always be lower
            # in this case than the elements from the sorted lists, and it will be put first, those also take up time
            print(
                f"In the worst case Strand Sort sorted a list of {length3} elements in {strand_sort_time3:.4f} seconds")
            print()
            i -= 1
            length3 *= 2