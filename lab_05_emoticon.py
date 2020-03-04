import random

eyes = [":", ";", "|", "X", "=", ">", "8","B", ]
noses = ["-", "'", "+", "~", "{",]
mouths = [")", "(", "S", "D", "C", "0", "o", "O", "P", ">", "|", "\\", "/",]

cycle = 0 

while cycle < 5:
    emoticon = random.choice(eyes) + random.choice(noses) + random.choice(mouths)
    print(emoticon)
    cycle += 1 