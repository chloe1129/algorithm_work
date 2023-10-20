h,b,c,s=input().split()
r = round(int(h)*int(b)*int(c)*int(s)/8/1024/1024,1)
print(f"{r} MB")