Mul = []
MulMax = []

for i in range(9):
    N = list(map(int, input().split()))
    Mul.append(N)
for a in range(9):
    MulMax.append(max(Mul[a]))

col = MulMax.index(max(MulMax))
row = Mul[col].index(max(Mul[col]))

print(max(MulMax))
print(col+1, row+1)