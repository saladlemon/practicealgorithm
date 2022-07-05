import sys
N = int(input())
for n in range(0, N):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d"%(n+1, A, B, A+B))
    n = n + 1