C = int(input())
for i in range(C):
    Score = list(map(int, input().split()))
    N = len(Score) - 1
    S = sum(Score) - Score[0]
    T = 0
    Average = S/N
    for j in range(1, len(Score)):
        if Score[j] > Average:
            T = T + 1
    per = (T/N)*100
    print('%.3f%%'%per)