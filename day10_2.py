from collections import deque

ops = open("day10").read().splitlines()

cycle = 0
xreg = 1
xbuffer = deque()
op_i = 0

crt = [["." for _ in range(40)] for _ in range(6)]


for cycle in range(240):
 
 #read or wait for op
 if (len(xbuffer) == 0):
  if (op_i >= len(ops)):
   break
  op = ops[op_i].split(" ")
  op_i += 1
  if (len(op) == 2): #addx n
   xbuffer.append(0)
   xbuffer.append(int(op[1]))
 
 #draw CRT
 column = cycle % 40
 if (abs(xreg - column) <= 1):
  crt[cycle // 40][column] = '#'

 #work on current addx
 if (len(xbuffer) > 0):
  xreg += xbuffer.popleft()
 
for crt_row in crt:
 print("".join(crt_row))