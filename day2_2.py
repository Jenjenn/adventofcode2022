#rock A 1
#paper B 2
#scissors C 3

#X lose
#Y draw
#Z win

scores = {
 "A X": 0 + 3,
 "A Y": 3 + 1,
 "A Z": 6 + 2,
 "B X": 0 + 1,
 "B Y": 3 + 2,
 "B Z": 6 + 3,
 "C X": 0 + 2,
 "C Y": 3 + 3,
 "C Z": 6 + 1,
}


f1 = open("day2")
lines = f1.read().splitlines()

score = 0


for line in lines:
 score += scores[line]

print(score)
