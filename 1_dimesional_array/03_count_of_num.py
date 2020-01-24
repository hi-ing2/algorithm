import sys
ls = []
total = 1
totals = []
dic = {}
for n in range(0,10):
    dic.setdefault(n, 0)
for i in range(3):
    ls.append(int(sys.stdin.readline()))
for j in range(len(ls)):
    total *= ls[j]
# print(total)
for k in str(total):
    for l in dic.keys():
        if l == int(k):
            dic[l] += 1  
for m in dic.values():
    print(m)

# count 함수 활용 버전
# a = int(input())
# b = int(input())
# c = int(input())

# k = a*b*c
# k_list = list(str(k))
# for i in range(10):
#     k_num_count = k_list.count(str(i))
#     print(k_num_count)