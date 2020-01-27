import sys

a = int(sys.stdin.readline().rstrip())
b = 0
c = a
count = 0
if a < 10:
    a = str(a).zfill(2) #0개수 채우기 (5 -> 05)
    print('zerocut')
while True: 
    b = 0
    num = ""
    for num in str(a):
        b += int(num) 
    a = int(str(int(a) % 10) + str(b % 10))
    count += 1
    if a == c:
        break

print(count)




