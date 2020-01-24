import sys

n, x = map(int, sys.stdin.readline().split())
count = 1
a = list(map(int, sys.stdin.readline().split()))
# 모범 답안
# for i in range(n):
#     if a[i] < x:
#         print(a[i], end=" ")

for j in a: # a.split는 리스트형태
    if count > n: # n개 보다 많이들어가면 값들을 버림
        break
    count += 1
    if int(j) < x:
        print(j, end=' ')# j의 값을 x와 비교해서 x보다 작으면 출력

