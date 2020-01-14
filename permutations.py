from string import ascii_lowercase
import itertools

al = list(ascii_lowercase)
sn = input('n을 입력하세요. 1 ≤ n ≤ 10')
n = int(sn)
real_al=[]
i = 0


if 1 <= n and n <= 10:
    for i in range(n):
        real_al.append(al[i])
print(real_al)


sr = input('r을 입력하세요. 0 ≤ r ≤ min(n, 7)')
r = int(sr)
if 0 <= r and r <= min(n, 7):
    print(list(map(''.join, itertools.permutations(real_al, r))))
final = list(map(''.join, itertools.permutations(real_al, r)))

for j in range(len(final)):
    if j == (len(final)-1):
        print(str(final[j]), end='')
    else:
        print(str(final[j])+', ',end='')
        
    
