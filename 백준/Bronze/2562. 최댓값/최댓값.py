A = []
for i in range(9):
    N = int(input())
    A.append(N)
    M = max(A)
print(M)
print(A.index(M)+1)

