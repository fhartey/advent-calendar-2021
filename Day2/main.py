filename = "./puzzle.txt"

with open(filename, "r") as f:
    content = f.read()

PositionF = 0
PoistionUpDown = 0
PositionAim = 0

for item in content.split("\n"):
    #print(item.split(" ")[0])
    if item.split(" ")[0] == "forward":
        PositionF = PositionF + int(item.split(" ")[1])
        PositionAim = PositionAim + (int(item.split(" ")[1]) * PoistionUpDown)

    if item.split(" ")[0] == "down":
        PoistionUpDown = PoistionUpDown + int(item.split(" ")[1])

    if item.split(" ")[0] == "up":
        PoistionUpDown = PoistionUpDown - int(item.split(" ")[1])

print(PositionF)
print(PoistionUpDown)
print("Answer")
print(PoistionUpDown * PositionF)
print("Answer2")
print(PositionF * PositionAim)
