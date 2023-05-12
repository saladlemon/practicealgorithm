S = str(input())
N = [-1 for _ in range(26)]

for b in range(len(S)):
    for a in range(97, 123):
        asc = chr(a)
        if S[b] == asc and N[a-97] == -1:
            N[a-97] = b
result = ' '.join(map(str, N))
print(result)