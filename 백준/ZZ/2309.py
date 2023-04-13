dwarfs =[]
for _ in range(9):
    dwarfs.append(int(input()))

dwarfs = sorted(dwarfs)
extra = sum(dwarfs)-100

def combination(arr, r):
    
    # 조합을 저장할 배열
    result = []
    
    # 실제 조합을 구하는 함수
    def combinate(c, index):
        if len(c) == r and c[0]+c[1]==extra:
            result.append(c)
            return 
        
        for idx, data in enumerate(arr):
            # 중복되는 조합이 생성되지 않게 마지막으로 들어온 원소의 인덱스보다
            # 새로 추가하는 원소의 인덱스가 큰 경우만 조합을 생성한다.
            if idx > index:
                combinate(c + [data], idx)
    
    combinate([], -1)
    
    return result

for i in list(set(dwarfs) - set(combination(dwarfs, 2)[0])):
    print(i)

    
