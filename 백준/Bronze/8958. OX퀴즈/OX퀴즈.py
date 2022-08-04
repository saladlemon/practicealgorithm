Num = int(input())
for Case in range(Num):
    Score = 0
    Sum = 0
    OX = list(input())
    for i in range(len(OX)):
        if OX[i] == 'O':
            Sum = Sum + 1
            Score = Score + Sum
        elif OX[i] == 'X':
            Sum = 0
    print(Score)