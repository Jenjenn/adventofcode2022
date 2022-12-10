f1 = open("day3")
sacks = f1.read().splitlines()

prio_sum = 0

for sack in sacks:
 c1 = set()
 
 for i in range(0, len(sack)//2):
  c1.add(sack[i])
  
 for i in range(len(sack)//2, len(sack)):
  if (sack[i] in c1):
   if (ord(sack[i]) < 97): #capital, ord('A') = 65, 
    prio_sum += ord(sack[i]) - 38
   else: #lowercase, ord('a') = 97
    prio_sum += ord(sack[i]) - 96
   break


print(prio_sum)