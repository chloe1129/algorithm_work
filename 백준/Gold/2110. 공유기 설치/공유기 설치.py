n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1
        # print(f'array: {array}')
        # print(f'start: {start}, end: {end}, mid: {mid}')
        for i in range(1, len(array)):
            # print(
            #     f'array[i]: {array[i]}, current: {current}, mid: {mid}, current+mid: {current+mid}')
            if array[i] >= current + mid:
                count += 1
                current = array[i]
                # print(f'count:{count}, current: {current}')

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
            # print(f'start: {start}, answer: {answer}')
        else:
            end = mid - 1
            # print(f'end:{end}')


start = 1
end = array[-1] - array[0]
answer = 0

binary_search(array, start, end)
print(answer)