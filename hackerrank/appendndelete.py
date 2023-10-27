def appendAndDelete(s, t, k):
    # Write your code here
    count = 0
    if s == t:
        print('11111111111jsut the same')
        return 'Yes'

    if s in t:
        print('if s in t', s, t)
        if len(t)-len(s) == k:
            print('if s in t is yes', s, t, k)
            return 'Yes'
        elif len(t)-len(s) < k and (k - (len(t)-len(s))) % 2 == 0:
            print('do to again 2')
            return 'Yes'
        else:
            print('s in t but t is too big', s, t, k)
            return 'No'
    elif s not in t:
        while (count <= k):
            s = s[:len(s)-1]
            count += 1
            print(f'lets check s: {s}, and count: {count}')

            if len(s) == 0:
                print(f'sss:{s}:ssss, count:{count}')
                if len(t) <= k - count:
                    return 'Yes'
                # elif len(t) < k - count and (k-count) % 2 == 0:
                #     return 'Yes'
                else:
                    return 'No'
            elif s in t and s[0] == t[0]:
                print('s in t????', s, t)
                if len(t)-len(s) == k-count:
                    return 'Yes'
                elif len(t)-len(s) < k-count and (k-count) % 2 == 0:
                    return 'Yes'
                elif len(t) <= k-count-len(t):
                    return 'Yes'
                else:
                    return 'No'

    if count == k:
        if s == t:
            return 'Yes'
        elif s != t:
            return 'No'
    return 'No'


print(appendAndDelete('aaa', 'a', 5))

# print(appendAndDelete('asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv',
#                       'bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv',
#                       100))
