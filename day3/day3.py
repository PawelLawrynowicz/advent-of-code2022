from pprint import pprint


def process_input(bags_path):
    file = open(bags_path, "r")
    bags = file.readlines()
    bags = [bag.removesuffix('\n') for bag in bags]
    return bags


def calculate_priority(duplicates):
    priority_sum = 0
    for letter in duplicates:
        if letter.islower():
            priority_sum += ord(letter) - 96
        else:
            priority_sum += ord(letter) - 38
    return priority_sum


def get_duplicates(bags):
    duplicates = str()
    for bag in bags:
        middle = len(bag) // 2
        bag_a = bag[:middle]
        bag_b = bag[middle:]
        duplicates += str(set(bag_a) & set(bag_b)
                          ).removeprefix("{'").removesuffix("'}")
    return duplicates


def group_bags(bags):
    grouped_bags = list()
    temp_list = list()
    for bag_number, bag in enumerate(bags, start=1):
        temp_list.append(bag)
        if bag_number % 3 == 0:
            grouped_bags.append(temp_list.copy())
            temp_list.clear()
    return grouped_bags


def find_badges(grouped_bags):
    shared = str()
    for group in grouped_bags:
        shared += str(set(group[0]) & set(group[1]) &
                      set(group[2])).removeprefix("{'").removesuffix("'}")
    return shared


if __name__ == "__main__":
    PATH = "day3/input"
    bags = process_input(PATH)
    badges = find_badges(group_bags(bags))
    print(calculate_priority(badges))
