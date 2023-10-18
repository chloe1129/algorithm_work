import sys


def find(x, y, n):
    global white, blue
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                find(x, y, n//2)
                find(x+n//2, y, n//2)
                find(x, y+n//2, n//2)
                find(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    paper = []
    for i in range(n):
        paper.append(list(map(int, sys.stdin.readline().split())))

    white = 0
    blue = 0
    find(0, 0, n)

    print(white)
    print(blue)
