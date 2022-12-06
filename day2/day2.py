shapePoints = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

shapes = {
    "Rock": 'X',
    "Paper": 'Y',
    "Scissors": 'Z'
}

commands = {
    "lose": 'X',
    "draw": 'Y',
    "win": 'Z'
}


def chooseShape(op, us):
    op = chr(ord(op)+23)
    if us == commands["lose"]:
        if op == shapes["Rock"]:
            return shapes["Scissors"]
        elif op == shapes["Paper"]:
            return shapes["Rock"]
        elif op == shapes["Scissors"]:
            return shapes["Paper"]
    elif us == commands["draw"]:
        return op
    elif us == commands["win"]:
        if op == shapes["Rock"]:
            return shapes["Paper"]
        elif op == shapes["Paper"]:
            return shapes["Scissors"]
        elif op == shapes["Scissors"]:
            return shapes["Rock"]


def gameOutcome(op, us):
    op = chr(ord(op) + 23)
    if op == us:
        return 3
    elif op == shapes["Rock"] and us == shapes["Paper"]:
        return 6
    elif op == shapes["Paper"] and us == shapes["Scissors"]:
        return 6
    elif op == shapes["Scissors"] and us == shapes["Rock"]:
        return 6
    else:
        return 0


points = 0
with open("day2/input") as f:
    games = f.readlines()
    for game in games:
        opponent = game[0]
        userMode = game[2]
        userChoice = chooseShape(opponent, userMode)
        points += shapePoints[userChoice]
        points += gameOutcome(opponent, userChoice)
print(points)
