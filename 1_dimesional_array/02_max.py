import sys

ls = []
for i in range(9):
    n = int(sys.stdin.readline()) 
    ls.append(n)

print(max(ls))

enu = list(enumerate(ls)) #index, value 모두 호출

for j in range(9):
    if max(ls) == enu[j][1]:
        print(enu[j][0]+1)
        break

# num_list = []
# for i in range(9):
#     num_list.append(int(input()))
    
# print(max(num_list))
# print(num_list.index(max(num_list))+1) #index 값 뽑을 수 있음
    