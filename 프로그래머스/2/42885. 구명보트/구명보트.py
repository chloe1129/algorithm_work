def solution(people, limit):
    people.sort()
    start = 0
    end = len(people)-1
    count=0
    while(start<=end):
        # print(start,end)
        rest = limit
        rest=rest-people[end]
        end-=1
        if rest >= people[start]:
            start+=1
        count+=1
    return count