a , b,c = input().split()
print((int(a) if int(a)<int(b) else int(b)) if((int(a) if int(a)<int(b) else int(b))<int(c)) else int(c))