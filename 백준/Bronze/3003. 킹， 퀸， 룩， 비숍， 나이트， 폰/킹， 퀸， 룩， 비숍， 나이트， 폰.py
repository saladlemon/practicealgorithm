chess = list(map(int, input().split()))
King = chess[0]
Queen = chess[1]
Rook = chess[2]
Bishop = chess[3]
Knight = chess[4]
Pawn = chess[5]
if King != 1:
    if King < 1:
        King = 1-King
    elif King > 1:
        King = -(King-1)
else:
    King = 0
if Queen != 1:
    if Queen < 1:
        Queen = 1-Queen
    elif Queen >1:
        Queen = -(Queen-1)
else:
    Queen = 0
if Rook != 2:
    if Rook < 2:
        Rook = 2-Rook
    elif Rook > 2:
        Rook = -(Rook - 2)
else:
    Rook = 0
if Bishop != 2:
    if Bishop < 2:
        Bishop = 2-Bishop
    elif Bishop > 2:
        Bishop = -(Bishop - 2)
else:
    Bishop = 0
if Knight != 2:
    if Knight < 2:
        Knight = 2 - Knight
    elif Knight >2:
        Knight = -(Knight - 2)
else:
    Knight = 0
if Pawn != 8:
    if Pawn < 8:
        Pawn = 8 - Pawn
    elif Pawn > 8:
        Pawn = -(Pawn - 8)
else:
    Pawn = 0
print(King, Queen, Rook, Bishop, Knight, Pawn)
