import sys
ls = []
for i in range(10):
    a = int(sys.stdin.readline())
    ls.append(a)
for j in range(10):
    ls[j] = ls[j] % 42
ls = set(ls) #집합(중복x)
print(len(ls))