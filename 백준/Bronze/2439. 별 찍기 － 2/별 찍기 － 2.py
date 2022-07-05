N = int(input())
for n in range(N, 0, -1):
    if n >= 0:
        print(" "*(n-1)+"*"*(N-n+1))