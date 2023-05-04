def solution(n, arr1, arr2):
    answer = []

    map1 = list(map(lambda x: bin(x)[2:], arr1))
    map2 = list(map(lambda x: bin(x)[2:], arr2))

    map1 = checkdigit(map1,n)
    map2 = checkdigit(map2,n)

    
    map1 = makearr(map1)
    map2 = makearr(map2)
    print(map1, map2)

    #makemap(map1)

    return answer

def checkdigit(arr, n):
    for i in range(len(arr)):
        if not len(arr[i]) == n:
            while(True):
                if(n-len(arr[i])==0):
                    break
                arr[i] = '0' + arr[i]
                
    return arr

def makearr(arr):
    strarr = []

    for i in range(len(arr)):
        strarr.append([*str(arr[i])])

    return strarr


def makemap(arr):
    map = []
    newstr = ''
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '0':
                newstr += '_'
            else:
                newstr += '#'
            
        map.append(newstr)
        newstr = ''
    print(map)

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))