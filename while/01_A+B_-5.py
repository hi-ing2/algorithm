import sys
ls_a= []
ls_b= []
while True:
    a, b= map(int, sys.stdin.readline().split())
    ls_a.append(a)
    ls_b.append(b)
    if ls_a[-1] == 0 and ls_b[-1] == 0:
        break

for c in range(len(ls_a)-1):
    print(ls_a[c] + ls_b[c])

for 