from functools import cmp_to_key

def isOrdered(left, right):
 for i in range(len(left)):
 
  if (i >= len(right)): return 1 #right side ran out
   
  if (isinstance(left[i], int) and isinstance(right[i], int)):
   if left[i] < right[i]:
    return -1
   elif left[i] > right[i]:
    return 1
   else:
    continue
  
  l,r = left[i],right[i]
  if (isinstance(l, int)): l = [l]
  if (isinstance(r, int)): r = [r]
  
  ordered = isOrdered(l, r)
  if (ordered != 0): return ordered
 
 if (len(left) < len(right)): return -1 #left side ran out
 
 return 0

dsignals = [[[2]],[[6]]]

inputs = open("day13").read().splitlines()
inputs = [eval(x) for x in inputs if x != ""]
inputs.extend(dsignals)
inputs.sort(key=cmp_to_key(isOrdered))

print((inputs.index(dsignals[0]) + 1) * (inputs.index(dsignals[1]) + 1))