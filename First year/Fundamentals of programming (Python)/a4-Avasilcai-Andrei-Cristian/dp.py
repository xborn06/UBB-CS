'''
Determine the longest common subsequence of two given sequences.
Subsequence elements are not required to occupy consecutive positions.
For example, if X = "MNPNQMN" and Y = "NQPMNM", the longest common subsequence has length 4, and can be one of "NQMN", "NPMN" or "NPNM".
Determine and display both the length of the longest common subsequence as well as at least one such subsequence.
'''


def naive_approach(x: str, y: str, len1: int, len2: int):
    if len1 == 0 or len2 == 0:
        return 0, ""
    if x[len1 - 1] == y[len2 - 1]:
        length, subsequence = naive_approach(x, y, len1 - 1, len2 - 1)
        return length + 1, subsequence + x[len1 - 1]
    length1, subsequence1 = naive_approach(x, y, len1, len2 - 1)
    length2, subsequence2 = naive_approach(x, y, len1 - 1, len2)
    if length1 > length2:
        return length1, subsequence1
    else:
        return length2, subsequence2


def dp(x: str, y: str):
    len1, len2 = len(x), len(y)
    dpmat = [[0] * (len2+1) for _ in range(len1 + 1)]
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if x[i - 1] == y[j - 1]:
                dpmat[i][j] = dpmat[i - 1][j - 1] + 1
            else:
                dpmat[i][j] = max(dpmat[i - 1][j], dpmat[i][j - 1])
    maxstr = []
    t =''
    i, j = len1, len2
    while i > 0 and j > 0:
        if x[i-1]==y[j-1]:
            maxstr.append(x[i-1])
            i-=1
            j-=1
        elif dpmat[i-1][j]>dpmat[i][j-1]:
            i-=1
        else:
            j-=1
    maxstr.reverse()
    maxlen=len(maxstr)
    for row in dpmat:
        print(row)
    return maxlen,t.join(maxstr)


c = 0
while not c == 1 and not c == 2:
    c = int(input("Which approach do you want to use?\n 1.Naive approach \n 2.Dynamic programming approach"))
    if c == 1:
        #x = str(input("Please insert the first sequence:\n"))
        #y = str(input("Please insert the second sequence:\n"))
        x="MNPNQMN"
        #x="ABCDEFKGOHJKLMNOPQ"
        y="NQPMNM"
        #y="BERCDAFMGIHMLKJONPQ"
        length, subsequence = naive_approach(x, y, len(x), len(y))
        if length > 0:
            print("The maximum subsequence is: ", subsequence, " and it has length ", length)

        else:
            print("There is no such subsequence")
    elif c == 2:
        #x = str(input("Please insert the first sequence:\n"))
        #y = str(input("Please insert the second sequence:\n"))
        x="MNPNQMN"
        #x="ABCDEFKGOHJKLMNOPQ"
        y="NQPMNM"
        #y="BRCDAFMGIHMLKJNPQ"
        lengthdp, subsequencedp = dp(x, y)
        if lengthdp > 0:
            print("The maximum subsequence is: ", subsequencedp, " and it has length ", lengthdp)
        else:
            print("There is no such subsequence")
    else:
        print("Input was not valid")
