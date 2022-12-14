import unittest


def get_task_dimensions(text):
    for line_number, line in enumerate(text):
        for char in line:
            if char.isdigit():
                task_width = int(text[line_number].removesuffix(
                    ' \n').split("   ")[-1])
                task_height = line_number
                return (task_width, task_height)


def gen_stacks(text):
    task_width, task_height = get_task_dimensions(text)
    stacks = list(list())
    for column in range(1, task_width*4 - 1, 4):
        stack = list()
        for row in range(task_height - 1, -1, -1):
            crate = text[row][column]
            if crate.isalpha():
                stack.append(crate)
        stacks.append(stack.copy())
        stack.clear()
    return stacks


def gen_commands(text):
    commands = list(list())
    for line in text:
        if line.startswith("move"):
            commands.append([int(n) for n in line.split()
                             if n.isdigit()])
    return commands


def move_crates_single_at_once(stacks, commands):
    for command in commands:
        crates_to_move = command[0]
        from_stack = command[1] - 1
        to_stack = command[2] - 1
        for i in range(crates_to_move):
            stacks[to_stack].append(stacks[from_stack].pop())
    return stacks


def move_crates_multiple_at_once(stacks, commands):
    for command in commands:
        crates_to_move = command[0]
        from_stack = command[1] - 1
        to_stack = command[2] - 1
        stacks[to_stack].extend(stacks[from_stack][-crates_to_move:])
        del stacks[from_stack][-crates_to_move:]
    return stacks


def get_top_crates(crates):
    top_crates = str()
    for stack in crates:
        top_crates += stack[-1]
    return top_crates


if __name__ == "__main__":
    PATH = "day5/input.txt"
    file = open(PATH, 'r')
    text = file.readlines()
    stacks = gen_stacks(text)
    commands = gen_commands(text)
    result = move_crates_multiple_at_once(stacks, commands)
    rearranged_crates = get_top_crates(result)
    print(get_top_crates(rearranged_crates))
