import sys
input = sys.stdin.readline

int_dict = {}
cnt = 0
while (True):
    name = input().strip()
    if not name:
        break

    if name in int_dict:
        int_dict[name] += 1
    else:
        int_dict[name] = 1
    cnt += 1
# print(dict(int_dict))
key = list(int_dict.keys())
key.sort()
for tree in key:
    print('%s %.4f' % (tree, (int(int_dict[tree])/cnt*100)))
