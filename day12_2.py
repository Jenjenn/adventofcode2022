from collections import deque

def isLegalMove(se,te):
 if (se == 'S'):
  if (te == 'a'):
   return True
  else:
   return False
 
 if (te == 'E'):
  if (se == 'z'):
   return True
  else:
   return False

 if ( ord(te) - ord(se) <= 1 ):
  return True

 return False


elev = [ [a for a in row] for row in ( open("day12").read().splitlines() ) ]
steps = [ [ 999999 for _ in range(len(elev[0])) ] for _ in range(len(elev)) ]
paths = deque()

start,end = None,None
#find start and end position
for i,row in enumerate(elev):
 for j,col in enumerate(row):
  if (col == 'E'):
   end = (i,j)
   paths.append((i,j,0))

fastest_a = 999999

while True and len(paths) > 0:
 i,j,st = paths.popleft()
 if (st < steps[i][j]): #unexplored or faster
  steps[i][j] = st
  if (elev[i][j] == 'a'):
   if (fastest_a > steps[i][j]):
    fastest_a = steps[i][j]
   continue
  #up
  if ( i > 0 and isLegalMove(elev[i-1][j], elev[i][j]) ):
   paths.append((i-1,j,st+1))
  #down
  if ( i < len(elev)-1 and isLegalMove(elev[i+1][j], elev[i][j]) ):
   paths.append((i+1,j,st+1))
  #left
  if ( j > 0 and isLegalMove(elev[i][j-1], elev[i][j]) ):
   paths.append((i,j-1,st+1))
  #right
  if ( j < len(elev[0])-1 and isLegalMove(elev[i][j+1], elev[i][j]) ):
   paths.append((i,j+1,st+1))
 else: #slower
  continue

print(fastest_a)