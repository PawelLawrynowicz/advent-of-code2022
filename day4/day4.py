def get_input(path):
    file = open(path, "r")
    assignments = [line.removesuffix('\n') for line in file.readlines()]
    return assignments


def calculate_redundant(assignments):
    redundant = 0
    for group in assignments:
        assignment1, assignmnet2 = group.split(',')
        assignment1_left, assignment1_right = assignment1.split('-')
        assignment2_left, assignment2_right = assignmnet2.split('-')
        if set(range(int(assignment1_left), int(assignment1_right)+1)).issubset(
            range(int(assignment2_left), int(assignment2_right)+1)) or \
            set(range(int(assignment2_left), int(assignment2_right)+1)).issubset(
                range(int(assignment1_left), int(assignment1_right)+1)):
            redundant += 1

    return redundant


if __name__ == "__main__":
    PATH = "day4/input"
    assignments = get_input(PATH)
    n_redundant = calculate_redundant(assignments)
    print(f"Elves that do redundant work: {n_redundant}")
