# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#    name = 'chloe'
#    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

T = int(input())

def getmax(cnt, num: int):
    global kind
    kind += str(num)
    if cnt >= n:
        print(sum(save))
        return save
    else:
        for i in range(1, 3):  # 두개의 비료
            if i == 1:
                if cnt == 0:
                    save.append((b1[cnt]))
                else:
                    # print(cnt-1)
                    if kind[cnt-1] == 1:
                        save.append(b1[cnt]-p)
                    else:
                        save.append(b1[cnt])
                getmax(cnt+1, 1)
            else:
                if cnt == 0:
                    save.append((b2[cnt]))
                else:
                    if kind[cnt-1] == 2:
                        save.append(b2[cnt]-p)
                    else:
                        save.append(b2[cnt])
                getmax(cnt+1, 2)


for test_case in range(1, T + 1):
    n, p = map(int, input().split())
    b1 = list(map(int, input().split()))
    b2 = list(map(int, input().split()))
    kind = ''  # 어떤 비료를 주었는지 저장
    save = []
    r1 = getmax(0, 1)
    r2 = getmax(0, 2)
    print((r1, r2))
    result = max(sum(r1), sum(r2))
    print(f'#{test_case} {result}')