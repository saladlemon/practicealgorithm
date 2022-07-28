A = int(input())
B = int(input())
C = int(input())
S = 0
N = A * B * C
L = list(map(int, str(N)))
for i in range(10):
    print(L.count(i))