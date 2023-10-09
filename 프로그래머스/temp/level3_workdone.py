import sys

# h : 이진트리의 높이, 2**h의 말단 직원, 1<=h<=10
# k : 말단 직원들이 각각 가진 업무의 개수, 1<=k<=10
# r : 업무가 진행되는 날, 1<=r<=1,000
# 홀수 날에는 왼쪽, 짝수 날에는 오른쪽 부하 직원이 올린 업무를 처리
# 총 r의 날에 처리된 업무 번호의 합을 계산


class Node:
    def __init__(self):
        self.depth = 0
        self.job = []
        self.left = []
        self.right = []


h, k, r = map(int, sys.stdin.readline().split())
tree = [Node() for _ in range(2**(h+1))]  # 트리 생성

for i in range(2**(h)):
    print((i+1)*h)
    work = list(map(int, sys.stdin.readline().split()))
    print('each work', work)
    tree[(i+1)*h].job = work[:]

    print(tree[(i+1)*h].job)
