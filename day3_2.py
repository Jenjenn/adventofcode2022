f1 = open("day3")
sacks = f1.read().splitlines()

prio_sum = 0

 
for i in range(0, len(sacks), 3):

 s12 = set()
 for item in sacks[i+1]:
  if (item in sacks[i]):
   s12.add(item)
 
 for item in sacks[i+2]:
  if (item in s12):
   if (ord(item) < 97): #capital, ord('A') = 65, 
    prio_sum += ord(item) - 38
   else: #lowercase, ord('a') = 97
    prio_sum += ord(item) - 96
   break


print(prio_sum)