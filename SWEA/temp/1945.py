import sys

T = int(sys.stdin.readline())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


for test_case in range(1, T + 1):
    prime = [2, 3, 5, 7, 11]
    save = [0, 0, 0, 0, 0]
    N = int(input())
    i = 4
    while (N > 1):
        print('this is N', N, prime[i])
        if N % prime[i] == 0:
            save[i] += 1
            N = N/prime[i]
        else:
            i -= 1
    print('#'+str(test_case)+' '+' '.join(list(map(str, save))))
