import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
ls = []
for i in range(n):
    ls.append(a[i]) 

print(min(ls), max(ls))