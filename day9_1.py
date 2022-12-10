moves = open("day9").read().splitlines()
moves = [[x[0], int(x[1])] for x in [move.split(" ") for move in moves]]

def adjustTail(Hx,Hy,Tx,Ty):
 dx = Hx - Tx
 dy = Hy - Ty
 if (abs(dx) + abs(dy) > 2):
  Tx += dx // abs(dx)
  Ty += dy // abs(dy)
 elif (abs(dx) > 1):
  Tx += dx // abs(dx)
 elif (abs(dy) > 1):
  Ty += dy // abs(dy)
 return Tx, Ty

Hx = 0
Hy = 0
Tx = 0
Ty = 0

touched = {(Tx,Ty)}

for move in moves:
 for _ in range(move[1]):
  if (move[0] == 'R'):
   Hx += 1
  elif (move[0] == 'L'):
   Hx -= 1
  elif (move[0] == 'U'):
   Hy += 1
  else:
   Hy -= 1
  Tx, Ty = adjustTail(Hx,Hy,Tx,Ty)
  touched.add((Tx,Ty))

print(len(touched))