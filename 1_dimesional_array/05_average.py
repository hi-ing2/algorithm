import sys

n = int(sys.stdin.readline())
a = sys.stdin.readline().split()
ls = []
avr_ls = []
count = 1
for i in a: # a.split는 리스트형태
    if count > n: # n개 보다 많이들어가면 값들을 버림
        break
    count += 1
    ls.append(int(i))
maximum = max(ls)
for j in range(len(ls)):
    avr_ls.append(float(ls[j]/maximum*100))
average = sum(avr_ls) / len(avr_ls)
print(average)