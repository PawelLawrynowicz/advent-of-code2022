with open("day1/input") as f:
    nElves = 0
    calorieSum = 0
    elves = dict()
    for line in f:
        if line == '\n':
            elves[nElves] = calorieSum
            calorieSum = 0
            nElves += 1
            continue
        calorieSum += int(line[:-1])
    elves = dict(sorted(elves.items(), key=lambda item: item[1], reverse=True))

    topThreeCalories = list(elves.values())[:3]
    topThreeElves = list(elves.keys())[:3]

    print(f"Top three elves with most calories:\n\
    Elf #{topThreeElves[0]}: {topThreeCalories[0]}\n\
    Elf #{topThreeElves[1]}: {topThreeCalories[1]}\n\
    Elf #{topThreeElves[2]}: {topThreeCalories[2]}\n\
    ")

    print(f"In total they are carrying: {sum(topThreeCalories)}")
