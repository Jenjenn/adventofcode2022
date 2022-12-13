def isOrdered(left, right):
 for i in range(len(left)):
 
  if (i >= len(right)): #right side ran out
   return False
   
  if (isinstance(left[i], int) and isinstance(right[i], int)):
   if left[i] < right[i]:
    return True
   elif left[i] > right[i]:
    return False
   else:
    continue
  
  if (isinstance(left[i], int)):
   left[i] = [left[i]]

  if (isinstance(right[i], int)):
   right[i] = [right[i]]
  
  ordered = isOrdered(left[i], right[i])
  if (ordered != None):
   return ordered
 
 if (len(left) < len(right)): #left side ran out
  return True
 
 return None

inputs = open("day13").read().splitlines()

correct = []

for j,i in enumerate(range(0, len(inputs), 3)):
 left, right = None, None
 left = eval(inputs[i])
 right = eval(inputs[i+1])
 
 if (isOrdered(left,right)):
  correct.append(j+1)

print(sum(correct))