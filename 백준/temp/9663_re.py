N = int(input())

def backtrack(n):
    for i in range(n):
        if n == 1:
            return 1
        else:
            