def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort()
    length = len(A)-1
    for i in range(length+1):
        # print(i)
        answer+=(A[i]*B[length-i])
        

    return answer