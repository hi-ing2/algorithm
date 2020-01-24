import sys
ls_a= []
ls_b= []

try:
    while True:
        a, b= map(int, sys.stdin.readline().split())
        print(a+b)
except:
    exit() #모든 오류(무한루프 포함)를 막아주는 excpet

