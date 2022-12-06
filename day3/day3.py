file = open("day3/input", "r")

bags = file.readlines()

bags = [bag.removesuffix('\n') for bag in bags]


def calculate_priority(duplicates):
    priority_sum = 0
    for letter in duplicates:
        if letter.islower():
            priority_sum += ord(letter) - 96
        else:
            priority_sum += ord(letter) - 38
    return priority_sum


duplicates = str()

for bag in bags:
    middle = len(bag) // 2
    bag_a = bag[:middle]
    bag_b = bag[middle:]
    duplicates += str(set(bag_a) & set(bag_b)
                      ).removeprefix("{'").removesuffix("'}")

print(calculate_priority(duplicates))
