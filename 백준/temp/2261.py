import sys
import math
import bisect

# print(bisect.bisect_left([1, 3, 4, 6, 7, 8, 0]))


def distance(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    nums.sort()
    print('sort by x', nums)

    if len(nums) == 2 or len(nums) == 3:
        if len(nums) == 2:
            print(distance(nums[0], nums[1]))
        else:
            print(min(min(distance(nums[0], nums[1]), distance(
                nums[1], nums[2])), distance(nums[0], nums[2])))

    else:
        mid = (nums[0][0]+nums[-1][0])//2
        print('this is mid', mid)

        print(bisect.bisect_left(list(nums.keys()), mid))
