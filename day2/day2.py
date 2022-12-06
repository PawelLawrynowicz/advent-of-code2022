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
        user = game[2]
        points += shapePoints[user]
        points += gameOutcome(opponent, user)
print(points)
