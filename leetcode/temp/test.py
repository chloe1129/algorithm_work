def mergesort(merge: list):

    if len(merge) < 2:
        return merge

    mid = len(merge)//2
    left = mergesort(merge[:mid])
    right = mergesort(merge[mid:])
    print(left, right)
    result = []
    l = r = 0
    while (l < len(left) and r < len(right)):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]

    return result


print(mergesort([1, 2, 5, 3, 9]))
