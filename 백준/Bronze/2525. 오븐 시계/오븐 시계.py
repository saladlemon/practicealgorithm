A, B = map(int, input().split())
C = int(input())
if 0 <= A <= 23 and 0 <= B <= 59 and 0 <= C <= 1000:
    if B + C >= 60:
        A = A + (( B + C ) / 60)
        B = ( B + C ) % 60
        if A > 23:
            A = int(A%24)
            print(A,B)
        else:
            print(int(A),B)
    else:
        print(A, B+C)