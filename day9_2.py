moves = open("day9").read().splitlines()
moves = [[x[0], int(x[1])] for x in [move.split(" ") for move in moves]]

def adjustKnot(k1, k2):
 dx = k1["x"] - k2["x"]
 dy = k1["y"] - k2["y"]
 if (abs(dx) + abs(dy) > 2):
  k2["x"] += dx // abs(dx)
  k2["y"] += dy // abs(dy)
 elif (abs(dx) > 1):
  k2["x"] += dx // abs(dx)
 elif (abs(dy) > 1):
  k2["y"] += dy // abs(dy)
 return k2

knots = [{"x":0,"y":0} for _ in range(10)]
touched = {(knots[-1]["x"], knots[-1]["y"])}

for move in moves:
 for _ in range(move[1]):
  if (move[0] == 'R'):
   knots[0]["x"] += 1
  elif (move[0] == 'L'):
   knots[0]["x"] -= 1
  elif (move[0] == 'U'):
   knots[0]["y"] += 1
  else:
   knots[0]["y"] -= 1
  for i in range(1, len(knots)):
   knots[i] = adjustKnot(knots[i-1],knots[i])
  touched.add((knots[-1]["x"], knots[-1]["y"]))

print(len(touched))