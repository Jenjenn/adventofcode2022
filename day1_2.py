f1 = open("day1")
lines = f1.readlines()
elves = [0]

for i, line in enumerate(lines):
 if (line == "\n"):
  elves.append(0)
 else:
  elves[len(elves)-1] += int(line)

elves2 = sorted(elves, key=int, reverse=True)

print(elves2[0] + elves2[1] + elves2[2])