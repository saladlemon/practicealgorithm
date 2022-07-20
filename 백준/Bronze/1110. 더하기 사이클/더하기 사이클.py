N = int(input())
if 0 <= N <= 99:
    New = 100
    Origin = N
    C = 0
    while Origin != New:
        if N < 10:
            New = 10*N + N
            N = New
            C = C +1
        else:
            T = N//10 #몫
            S = int(N%10) #나머지
            M = T + S #몫 + 나머지
            New = 10*S + int(M%10)
            N = New
            C = C + 1
print(C)