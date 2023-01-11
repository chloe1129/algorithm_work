def solution(d, budget):
    answer = 0
    count = 0

    if sum(d)< budget:
        count=len(d)
    else:
        d=sorted(d)
        for i in d:
            answer+=i
            count+=1
            if answer>budget:
                count-=1
                break
    return count


#print(solution([1,3,2,5,4],9))
#print(solution([2,2,3,3],10))
print(solution([1,1],10))
