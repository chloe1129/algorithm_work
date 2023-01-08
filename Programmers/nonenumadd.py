def solution(numbers):
    answer = [0,1,2,3,4,5,6,7,8,9]
    count=0
    for i in answer:
        if i in numbers:
            pass
        else:
            count += i
    return count

print(solution([5,8,4,0,6,7,9]))

'''
하나하나 더하는게 아니라 총 합에서 빼는 경우!
def solution(numbers):
    return 45 - sum(numbers)
'''