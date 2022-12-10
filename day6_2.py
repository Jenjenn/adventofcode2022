f1 = open("day6")
buf = f1.read()

marker = 0
marker_size = 14

for i in range(marker_size,len(buf)):
 s1 = set(buf[i-marker_size:i])
 if (len(s1) == marker_size):
  marker = i
  break
 
print(marker)