T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    P = ""
    for j in range(len(S)):
        P = P + S[j]*R
    print(P)
