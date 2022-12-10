#rock A X 1
#paper B Y 2
#scissors C Z 3

scores = {
 "A X": 3 + 1,
 "A Y": 6 + 2,
 "A Z": 0 + 3,
 "B X": 0 + 1,
 "B Y": 3 + 2,
 "B Z": 6 + 3,
 "C X": 6 + 1,
 "C Y": 0 + 2,
 "C Z": 3 + 3,
}


f1 = open("day2")
lines = f1.read().splitlines()

score = 0


for line in lines:
 score += scores[line]

print(score)
