A, B = map(str, input().split())
A = ''.join(reversed(A))
B = ''.join(reversed(B))
if A > B:
    print(A)
else:
    print(B)
