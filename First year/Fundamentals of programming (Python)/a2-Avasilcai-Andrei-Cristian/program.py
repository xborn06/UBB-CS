import random
import math


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
    for i in range(len(sorted_l)):
        l.append(sorted_l[i])
    return l


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


def jump_search(x: int, l: list) -> int:
    step = int(math.sqrt(len(l)))
    length = len(l)
    s1 = 0
    s2 = step
    while s2 < length and l[s2] < x:
        s1 = s2
        s2 += step
    s2 = min(s2,length)
    for i in range(s1, s2+1):
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
    n = int(input("What would you like to do?"))
    if n>5:
        n=int(input("That isn't an available option. Please try again:"))
    if n == 5:
        print("The program has ended")
        break
    if n == 1:
        print("What should the length of the list be?")
        length = int(input())
        while length <= 0:
            length=int(input("Please insert a valid value"))
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
