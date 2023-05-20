
AB = []
S = []

N, M = map(int, input().split())
for i in range(0, N*2):
    component = list(map(int, input().split()))
    AB.append(component)
A = AB[:N]
B = AB[N:]
for a in range(N):
    for b in range(M):
        Sum_arr = A[a][b]+B[a][b]
        S.append(Sum_arr)
A = S[:N]
B = S[N:]
A = ' '.join(map(str, A))
B = ' '.join(map(str, B))
print(A)
print(B)