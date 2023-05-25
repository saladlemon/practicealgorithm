N = [[] for _ in range(15)]

for i in range(5):
    A = input()
    for j in range(len(A)):
        N[j].append(A[j])
for a in N:
    result = ''.join(map(str, a))
    print(result, end='')