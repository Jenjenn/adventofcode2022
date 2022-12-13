from collections import deque

ops = open("day10").read().splitlines()

cycle = 0
cycles = [20,60,100,140,180,220]
cycles.reverse()
xreg = 1
xbuffer = deque()
ssum = 0
i = 0


while (True):
 cycle += 1
 if (cycle >= cycles[-1]):
  print((cycle, xreg, cycle * xreg))
  ssum += cycle * xreg
  cycles.pop()
  if (len(cycles) == 0):
   break
 
 if (len(xbuffer) == 0):
  if (i >= len(ops)):
   break
  op = ops[i].split(" ")
  i += 1
  if (len(op) == 2): #addx n
   xbuffer.append(0)
   xbuffer.append(int(op[1]))

 if (len(xbuffer) > 0):
  xreg += xbuffer.popleft()
 

print(ssum)