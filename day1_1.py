f1 = open("day1")
lines = f1.readlines()
maxsum = 0
elves = [0]

for i, line in enumerate(lines):
 if (line == "\n"):
  if (elves[len(elves)-1] > maxsum):
   maxsum = elves[len(elves)-1]
  elves.append(0)
 else:
  elves[len(elves)-1] += int(line)

if (elves[len(elves)-1] > maxsum):
 maxsum = elves[len(elves)-1]

print(maxsum)