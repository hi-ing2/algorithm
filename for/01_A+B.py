import sys

n = int(sys.stdin.readline())
ls_a = []
ls_b = []
for i in range(0, n): 
    a, b = map(int, sys.stdin.readline().split(' '))
    ls_a.append(a)
    ls_b.append(b)
for j in range(0, n):
    print("Case #%d: %d + %d = %d" %((j+1), ls_a[j], ls_b[j], (ls_a[j] + ls_b[j])))