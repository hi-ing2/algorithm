# a, b = map(int, input().split(' '))
a = int(input())
b = int(input())
ls = []
# b % 10 == 5
# (b // 10) % 10 == 8
# ((b // 10) // 10) % 10 == 3 
class aaa:
    def double(self, a, b):
        bv = b
        for i in range(1, len(str(b))+1):
            br = bv % 10
            ls.append(a*br)
            bv = bv //10
        ls.append(a*b)
        return ls

A = aaa()
ans = A.double(a, b)
print(ans)