A, B, C  = map(int, input().split())
if A == B == C:
    P = 10000+A*1000
    print(P)
elif A == B != C:
    P = 1000+A*100
    print(P)
elif A == C != B:
    P = 1000+A*100
    print(P)
elif B == C != A:
    P = 1000+B*100
    print(P)
elif A != B != C:
    if A>B>C or A>C>B:
        print(A*100)
    elif B>A>C or B>C>A:
        print(B*100)
    elif C>A>B or C>B>A:
        print(C*100)