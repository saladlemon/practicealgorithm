X = int(input())
N = int(input())
S = 0
for i in range(N):
    a, b = map(int, input().split())
    C = a * b
    S = S + C
if X == S:
    print("Yes")
else:
    print("No")