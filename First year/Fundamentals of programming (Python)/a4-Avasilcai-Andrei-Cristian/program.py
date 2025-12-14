def is_valid(sol: list, n: int) -> bool:
    if len(sol)>0:
        if sum(sol) % n == 0:
            return True
        else:
            return False
    return False

def iterative_backtracking (l:list, n: int):
    stack = [([],0)]
    while stack:
        subset, index = stack.pop()
        if is_valid(subset,n):
            print(subset)
        for i in range(index,len(l)):
            stack.append((subset + [l[i]],i+1))

def recursive_backtracking(index: int, l: list, n: int, solution: list):
    for i in range(index, len(l)):
        solution.append(l[i])
        if is_valid(solution, n):
            print(solution)
        recursive_backtracking(i + 1, l, n, solution)
        solution.pop()

print("Please insert the list:")
l = [int(x) for x in input().split()]
n = int(input("What should the value of n be?"))
iterative_backtracking(l, n)
print()
sol = []
recursive_backtracking(0, l, n, sol)
