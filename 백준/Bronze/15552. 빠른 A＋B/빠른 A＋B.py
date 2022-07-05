import sys
T = int(input())
n = 1
while n <= T:
    A, B = map(int, sys.stdin.readline().split())
    n = n + 1
    print(A+B) 