f1 = open("day6")
buf = f1.read()

marker = 0

for i in range(4,len(buf)):
 s1 = set(buf[i-4:i])
 if (len(s1) == 4):
  marker = i
  break
 
print(marker)