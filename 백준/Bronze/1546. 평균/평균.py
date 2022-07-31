Num = int(input())
Score = list(map(int, input().split()))
M = max(Score)
Sum = 0
NScore = []
for i in range(Num):
    if i != Num:
        NScore.append((Score[i]/M)*100)
        Sum = Sum + NScore[i]
print(Sum/Num)
