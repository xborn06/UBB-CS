#
# Write the implementation for A5 in this file
#
#
# Write below this comment
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
import math
'''
def create_number(nrstr: str):
    re, img = 0, 0
    if "i" not in nrstr:
        re = int(nrstr)
        img = 0
        return [re, img]
    nrstr = nrstr.replace("i", "")
    if nrstr == "":
        re, img = 0, 1
        return [re, img]
    elif nrstr == "-":
        re, img = 0, -1
        return [re, img]
    if nrstr.isdigit() or (nrstr.startswith('-') and nrstr[1:].isdigit()):
        re = 0
        img = int(nrstr)
        return [re, img]
    if '+' in nrstr[1:]:
        split_pos = nrstr.find('+', 1)
    elif '-' in nrstr[1:]:
        split_pos = nrstr.find('-', 1)
    else:
        raise ValueError("Invalid complex number format")
    re = int(nrstr[:split_pos])
    imag_part_str = nrstr[split_pos:]
    if imag_part_str == "+":
        img = 1
    elif imag_part_str == "-":
        img = -1
    else:
        img = int(imag_part_str)
    return [re, img]


def get_real(nr: list):
    return nr[0]


def get_img(nr: list):
    return nr[1]


def set_real(nr: list, value: int):
    nr[0] = value


def set_img(nr: list, value: int):
    nr[1] = value


def to_string(number: list):
    if len(number) != 2:
        raise ValueError("Invalid complex number format: expected a list with [real, imag]")
    real, imag = number[0], number[1]
    if real == 0 and imag == 0:
        return "0"
    elif real == 0:
        if imag == 1:
            return "i"
        elif imag == -1:
            return "-i"
        else:
            return f"{imag}i"
    elif imag == 0:
        return str(real)
    else:
        if imag > 0:
            if imag == 1:
                imag_str = "+i"
            else:
                imag_str = f"+{imag}i"
        elif imag == -1:
            imag_str = f"-i"
        else:
            imag_str = f"{imag}i"
        return f"{real}{imag_str}"


#
# Write below this comment
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
'''
def create_number(nrstr: str):
    nr = {
        "re": 0,
        "img": 0
    }
    if nrstr.isdigit():
        nr["re"]=int(nrstr)
        nr["img"]=0
        return nr
    nrstr = nrstr.replace("i", "")
    if nrstr == "":
        nr["re"]=0
        nr["img"]=1
        return nr
    elif nrstr == "-":
        nr["re"] = 0
        nr["img"] = -1
        return nr
    if nrstr.isdigit() or (nrstr.startswith('-') and nrstr[1:].isdigit()):
        nr["re"] = 0
        nr["img"] = int(nrstr)
        return nr
    if '+' in nrstr[1:]:
        split_pos = nrstr.find('+', 1)
    elif '-' in nrstr[1:]:
        split_pos = nrstr.find('-', 1)
    else:
        raise ValueError("Invalid complex number format")
    nr["re"] = int(nrstr[:split_pos])
    imag_part_str = nrstr[split_pos:]
    if imag_part_str == "+":
        nr["img"] = 1
    elif imag_part_str == "-":
        nr["img"] = -1
    else:
        nr["img"] = int(imag_part_str)
    return nr

def get_real(nr: dict):
    return nr["re"]

def get_img(nr: dict):
    return nr["img"]

def set_real (nr:dict, value: int):
    nr["re"]=value

def set_img(nr:dict, value:int):
    nr["img"]=value

def to_string(nr:dict):
    if len(nr) != 2:
        raise ValueError("Invalid complex number format")
    real, imag = nr["re"], nr["img"]
    if real == 0 and imag == 0:
        return "0"
    elif real == 0:
        if imag == 1:
            return "i"
        elif imag == -1:
            return "-i"
        else:
            return f"{imag}i"
    elif imag == 0:
        return str(real)
    else:
        if imag > 0:
            if imag == 1:
                imag_str = "+i"
            else:
                imag_str = f"+{imag}i"
        elif imag == -1:
            imag_str = f"-i"
        else:
            imag_str = f"{imag}i"
        return f"{real}{imag_str}"


#
# Write below this comment
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def subarrseq(nr_list: list):
    longest_subarray = detlopgsuba(nr_list)
    longest_subsequence = detlongsubs(nr_list)
    return longest_subarray, longest_subsequence

def modulus(number):
    real = get_real(number)
    imag = get_img(number)
    return math.sqrt(real ** 2 + imag ** 2)


def check(maxlist:list, current_element):
    for i in range(len(maxlist)):
        if get_real(maxlist[i]) == get_real(current_element) and get_img(maxlist[i]) == get_img(current_element):
            #print(current_element,maxlist)
            return False
    return True

def detlopgsuba(glist: list):
    current_list = []
    max_list = []
    for i in range(len(glist)):
        current_element = create_number(glist[i])
        if check(current_list, current_element):
            current_list.append(current_element)
        else:
            if len(current_list) > len(max_list):
                max_list = current_list
            current_list = [current_element]
    if len(current_list) > len(max_list):
        max_list = current_list
    max_arr = []
    for i in range(len(max_list)):
        max_arr.append(to_string(max_list[i]))
    return max_arr


def detlongsubs(glist: list):
    mod_list = [modulus(create_number(number)) for number in glist]
    n = len(mod_list)
    if n == 0:
        return []
    dp = []
    parent = [-1] * n
    indices = [-1] * n
    for i in range(n):
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < mod_list[i]:
                left = mid + 1
            else:
                right = mid
        if left < len(dp):
            dp[left] = mod_list[i]
            indices[left] = i
            parent[i] = indices[left-1] if left > 0 else -1
        else:
            dp.append(mod_list[i])
            indices[len(dp) - 1] = i
            parent[i] = indices[len(dp) - 2] if len(dp) > 1 else -1
    lis = []
    index = indices[len(dp) - 1]
    while index != -1:
        lis.append(glist[index])
        index = parent[index]
    lis.reverse()
    return lis


#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#
def options():
    print("1.Read a list of complex numbers")
    print("2.Display the list")
    print("3.Show the longest subarray of distinct numbers and the longest increasing sequence, when considering each number's modulus")
    print("4.Exit")


def read_list():
    strlist = [str(x) for x in input("Enter complex numbers: ").split()]
    return strlist


def show_list(number_list: list):
    print(" ".join(number_list))


def user_option():
    user_input = 0
    ok = 0
    while user_input != 4:
        options()
        user_input = input("Which option do you want to choose?\n")
        try:
            user_input = int(user_input)
        except ValueError:
            print("The given input is not a number")
        if user_input > 4:
            print("There is no such option")
        elif user_input < 4:
            if user_input == 1:
                complex_list = read_list()
                ok = 1
            if ok == 1:
                if user_input == 2:
                    show_list(complex_list)
                if user_input == 3:
                    l1 = detlopgsuba(complex_list)
                    l2 = detlongsubs(complex_list)
                    show_list(l1)
                    show_list(l2)
            else:
                print("No list was to work with")

if __name__ == "__main__":
    user_option()
#3+4i 1+i 2+5i 6i 3+4i 3-4i 1-i 5+12i -1+i 4+3i 2i