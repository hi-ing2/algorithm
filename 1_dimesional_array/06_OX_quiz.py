import sys

N = int(sys.stdin.readline())

for i in range(N):
    ox = sys.stdin.readline().rstrip('\n')
    score_sum = 0
    score = 0
    ls = []
    for j in ox:
        ls.append(j)
    for j in range(len(ls)):
        if ls[j] == 'O':
            score += 1
            score_sum += score
        else:
            score = 0
    print(score_sum)



            
            