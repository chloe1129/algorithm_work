import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())

set_lst = set(lst) ## set으로 변환해서 중복 값 제거
lst = list(set_lst)

# 상위조건과 하위 조건이 있으면 하위 조건으로 정렬 후 상위 조건으로 정렬
lst.sort() # 알파벳 순서로 정렬
lst.sort(key = len) # 문자열 길이 순으로 정렬

for i in lst:
    print(i)