def get_input(path):
    file = open(path, "r")
    assignments = [line.removesuffix('\n') for line in file.readlines()]
    return assignments


def split_to_ranges(group):
    assignment1, assignmnet2 = group.split(',')
    assignment1_left, assignment1_right = assignment1.split('-')
    assignment2_left, assignment2_right = assignmnet2.split('-')
    range1 = range(int(assignment1_left), int(assignment1_right)+1)
    range2 = range(int(assignment2_left), int(assignment2_right)+1)

    return (range1, range2)


def calculate_redundant(assignments):
    redundant = 0
    for group in assignments:
        range1, range2 = split_to_ranges(group)
        if set(range1).issubset(range2) or set(range2).issubset(range1):
            redundant += 1

    return redundant


def calculate_overlaping(assignments):
    overlaping = 0
    for group in assignments:
        range1, range2 = split_to_ranges(group)
        if set(range1).intersection(range2):
            overlaping += 1
    return overlaping


if __name__ == "__main__":
    PATH = "day4/input"
    assignments = get_input(PATH)
    n_redundant = calculate_redundant(assignments)
    n_overlaping = calculate_overlaping(assignments)
    print(
        f"Elves that do redundant work: {n_redundant}\nElves that have overlaping work: {n_overlaping}")
