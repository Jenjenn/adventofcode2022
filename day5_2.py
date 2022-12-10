f1 = open("day5")
lines = f1.read().splitlines()

blankline = 0
stacks = {}

#init empty stacks
for i in range((len(lines[0]) + 1) // 4):
 stacks[i+1] = []

#find the blank line
for i in range(0, len(lines)):
 if (lines[i] == ""):
  blankline = i
  break

#populate the stacks
for i in range(blankline - 2, -1, -1):
 line = lines[i]
 for j,k in enumerate(range(1,len(line),4)):
  if (line[k] != " "):
   stacks[j+1].append(line[k])

#execute the moves
for i in range(blankline + 1, len(lines)):
 tokens = lines[i].split(" ")
 amount = int(tokens[1])
 src = int(tokens[3])
 dest = int(tokens[5])
 stacks[dest].extend(stacks[src][-1 * amount:])
 stacks[src] = stacks[src][:-1 * amount]

#build the output
output = ""
for i in range(len(stacks)):
 if (len(stacks[i+1]) > 0):
  output += stacks[i+1][-1]
 
print(output)