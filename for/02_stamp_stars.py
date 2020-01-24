import sys

n = int(sys.stdin.readline())
star = ""
for i in range(1,n+1): 
    for j in range(0,n-i):
        print(' ', end='')
    star += "*"
    print(star) 