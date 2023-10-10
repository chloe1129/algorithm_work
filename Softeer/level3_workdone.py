import sys

# h : 이진트리의 높이, 2**h의 말단 직원, 1<=h<=10
# k : 말단 직원들이 각각 가진 업무의 개수, 1<=k<=10
# r : 업무가 진행되는 날, 1<=r<=1,000
# 홀수 날에는 왼쪽, 짝수 날에는 오른쪽 부하 직원이 올린 업무를 처리
# 총 r의 날에 처리된 업무 번호의 합을 계산


def today_work(tree, worker, day):  # 오늘 할 일
    global work_done
    global done
    work_done = tree[:]  # 얕은복사 해주기
    # print('whuwhy', work_done[0].job)
    # 모든 직원들이 업무를 처리한다
    for i in range(1, worker+1):  # 모든 직원들에 대해서 업무를 처리하게 한다.

        if (len(work_done[i].job) > 0 or work_done[i].depth == h):  # 노드의 job에 업무가 있다면 말단사원
            up = 0
            # 현재 자신의 업무만만 처리해해 그냥 상사한테테 up
            if len(work_done[i].job) > 0:
                up = work_done[i].job[0]
                if len(work_done[i].job) > 1:
                    work_done[i].job = work_done[i].job[1:]
                    # print('del???',work_done[i].job)
                else:
                    work_done[i].job = []
                    # print('empty???',work_done[i].job)
                work_up(i, up)  # 상사한테 올리기

        else:
            up = 0
            # 짝수날, 오른쪽노드, 노드번호홀수
            if (day % 2 == 0) and len(work_done[i].right) > 0:
                up = work_done[i].right[0]
                if i == 1:
                    # print('how many times',i,up,day)
                    done += up
                else:
                    work_up(i, up)  # i가 1, 부서장이이 아니라면 상사한테 올리기

                if len(work_done[i].right) > 1:  # 완료한 업무 삭제
                    work_done[i].right = work_done[i].right[1:]
                   #  print('del',work_done[i].right)
                else:
                    work_done[i].right = []
                    # print('del right',work_done[i].right)

            # 홀수날, 왼쪽노드, 노드번호짝수
            elif (day % 2 != 0) and len(work_done[i].left) > 0:
                up = work_done[i].left[0]

                if i == 1:
                    # print('how many times',i,up,day)
                    done += up
                else:
                    work_up(i, up)  # i가 1, 부서장이이 아니라면 상사한테 올리기

                if len(work_done[i].left) > 1:  # 완료한 업무 삭제
                    work_done[i].left = work_done[i].left[1:]
                    # print('del',work_done[i].left)
                else:
                    work_done[i].left = []
                    # print('del left',work_done[i].left)

    return work_done  # 오늘 업무를 처리해서 위로 올린 tree를 리턴, 재귀 형식으로 날짜별로 반복해서 처리


def work_up(node_num, work_num):
    if node_num % 2 != 0:
        work_done[int((node_num-1)/2)].right.append(work_num)
    else:
        work_done[int((node_num)/2)].left.append(work_num)


class Node:
    def __init__(self):
        self.depth = 0
        self.job = []  # 말단직원이 맡은 업무
        # 부하직원이 올린 업무 홀-왼/짝-오 구분해서 저장
        self.left = []
        self.right = []


h, k, r = map(int, sys.stdin.readline().split())
tree = [Node() for _ in range(2**(h+1))]  # 트리 생성

done = 0  # 부서장이 완료한 번호
for i in range(2**(h)):  # 말단 직원수에 맞게 업무 처음으로 분배
    work = list(map(int, sys.stdin.readline().split()))
    # print('each work', 2**h+i)  # 말단직원 시작번호
    tree[2**h+i].job = work[:]  # 말단직원 초기 업무
    tree[2**h+i].depth = h  # 말단직원의 깊이
    # print('went in??', work, tree[2**h+i].job)

for j in range(0, r):  # 날짜
    today_work(tree, 2**(h+1)-1, j+1)  # 현재 트리의 상태, 전 직원의 수, 홀짝구분을을 위해 업무날짜

print(done)
