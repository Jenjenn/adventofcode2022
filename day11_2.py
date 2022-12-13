from collections import deque

inf = open("day11").read().splitlines()

monkeys = []
lcm = 1

mi = 0
while (mi < len(inf)):
 monkeys.append(dict())
 monkeys[-1]["items"] = deque([int(x) for x in (inf[mi+1][18:].split(","))])
 monkeys[-1]["op"] = inf[mi+2][19:]
 monkeys[-1]["divby"] = int(inf[mi+3].split(" ")[-1])
 lcm *= monkeys[-1]["divby"]
 monkeys[-1][True] = int(inf[mi+4].split(" ")[-1])
 monkeys[-1][False] = int(inf[mi+5].split(" ")[-1])
 monkeys[-1]["inspections"] = 0
 mi += 7

for i in range(10000):
 print(i)
 for monkey in monkeys:
  #for each item => op(item) => div by 3 => div by? => new monkey
  while (len(monkey["items"]) > 0):
   old = monkey["items"].popleft()
   old = eval(monkey["op"]) % lcm
   monkeys[monkey[old % monkey["divby"] == 0]]["items"].append(old)
   monkey["inspections"] += 1

i = [m["inspections"] for m in monkeys]
i.sort(reverse=True)


print(i[0] * i[1])