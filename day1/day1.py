with open("day1/input", "r") as f:
    nElves = elfNumber = mostCalories = currentCalories = 0

    for line in f:
        if line == '\n':
            mostCalories = max(currentCalories, mostCalories)
            if currentCalories == mostCalories:
                elfNumber = nElves
            currentCalories = 0
            nElves += 1
            continue
        currentCalories += int(line[:-1])

    print(f"Most calories are carried by Elf #{elfNumber}: {mostCalories}")
