f1 = open("day4")
pairs = f1.read().splitlines()

overlaps = 0

for pair in pairs:

 c1 = pair.replace("-", ",")
 c1 = c1.split(",")
 c2 = int(c1[1])
 c3 = int(c1[2])
 c4 = int(c1[3])
 c1 = int(c1[0])

 if (c3 >= c1 and c4 <= c2):
  overlaps += 1
 elif (c1 >= c3 and c2 <= c4):
  overlaps += 1


print(overlaps)