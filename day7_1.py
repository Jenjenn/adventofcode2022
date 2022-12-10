class Node:
 def __init__(self, n, p=None):
  self.name = n
  self.parent = p
  self.size_all = 0
  self.children = []
  self.size_f = 0
 
lines = open("day7").read().splitlines()

cdir = Node("/")
file_sizes = 0
dir_sizes = []

for line in lines:
 t = line.split(" ")
 
 if (t[0] == "$"):
  if (t[1] == "cd"):
   if (t[2] == "/"):
    continue
   else:
    if (t[2] == ".."):
     cdir.size_f = file_sizes
     dir_sizes.append(file_sizes)
     cdir = cdir.parent
     file_sizes += cdir.size_f
    else:
     cdir.size_f = file_sizes
     cdir.children.append(Node(t[2], cdir))
     cdir = cdir.children[-1]
     file_sizes = 0
   
 elif (t[0].isnumeric()):
  file_sizes += int(t[0])

#might not be back at root directory, mimic "cd .." commands
while (cdir.parent != None):
 cdir.size_f = file_sizes
 dir_sizes.append(file_sizes)
 cdir = cdir.parent
 file_sizes += cdir.size_f
 cdir.size_f = file_sizes

dir_sizes = [d for d in dir_sizes if d <= 100000]

print(sum(dir_sizes))