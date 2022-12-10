trees = open("day8").read().splitlines()
trees = [[int(x) for x in row] for row in trees]

fh = len(trees)
fw = len(trees[0])

ss = [ [0] * fh for _ in range(fw)]

max_ss = 0
for y in range(1,fh-1):
 for x in range(1,fw-1):
  ss = 0
  #look north
  for yy in range(y-1, -1, -1):
   if (trees[y][x] <= trees[yy][x] or yy == 0):
    ss = y - yy
    break

  #look south
  for yy in range(y+1, fh):
   if (trees[y][x] <= trees[yy][x] or yy == fh-1):
    ss *= yy - y
    break

  #look west
  for xx in range(x-1, -1, -1):
   if (trees[y][x] <= trees[y][xx] or xx == 0):
    ss *= x - xx
    break

  #look east
  for xx in range(x+1, fw):
   if (trees[y][x] <= trees[y][xx] or xx == fw-1):
    ss *= xx - x
    break
  
  print(str(trees[y][x]) + " at x,y=" + str(x) + "," + str(y) + " score is " + str(ss))
  
  if (ss > max_ss):
   max_ss = ss

print(max_ss)