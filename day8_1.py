trees = open("day8").read().splitlines()
trees = [[int(x) for x in row] for row in trees]

fh = len(trees)
fw = len(trees[0])

visible = [ [0] * fh for _ in range(fw)]

#left
for i in range(fh):
 tallest = -1
 for j in range(fw):
  if (trees[i][j] > tallest):
   visible[i][j] = 1
   tallest = trees[i][j]
   if (tallest == 9):
    break

#right
for i in range(fh):
 tallest = -1
 for j in range(fw-1, -1, -1):
  if (trees[i][j] > tallest):
   visible[i][j] = 1
   tallest = trees[i][j]
   if (tallest == 9):
    break

#top
for j in range(fw):
 tallest = -1
 for i in range(fh):
  if (trees[i][j] > tallest):
   visible[i][j] = 1
   tallest = trees[i][j]
   if (tallest == 9):
    break

#bottom
for j in range(fw):
 tallest = -1
 for i in range(fh-1, -1, -1):
  if (trees[i][j] > tallest):
   visible[i][j] = 1
   tallest = trees[i][j]
   if (tallest == 9):
    break

num_visible = sum(sum(row) for row in visible)

print(num_visible)