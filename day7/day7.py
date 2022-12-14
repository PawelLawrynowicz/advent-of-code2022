from anytree import NodeMixin, Node, find, RenderTree, PostOrderIter, PreOrderIter, find_by_attr

SIZE_THRESHOLD = 100_000
FILE_SYSTEM_SIZE = 70_000_000
NEEDED_SPACE = 30_000_000

commands = open("day7/input", "r")


# Directory class with content_size
class Directory(Node, NodeMixin):
    def __init__(self, name, content_size=0, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.content_size = content_size


# Set the root folder:
root = None
first_line = commands.readline()
try:
    root_directory = first_line.split(' ')[-1].removesuffix('\n')
    root = Directory(name=root_directory, content_size=0)
except not first_line.startswith("$ cd"):
    print("The first line should navigate to the root folder")

current_dir = root

# Create a tree from commands
for line in commands:
    if line.startswith("$ cd"):
        dir_to_move = line.split(' ')[-1].removesuffix('\n')
        if dir_to_move == "..":
            # go back to parent dir
            current_dir = current_dir.parent
        else:
            # enter the directory
            current_dir = find(
                current_dir, filter_=lambda node: node.name == dir_to_move and node.parent == current_dir)
    elif line.startswith("$ ls"):
        continue
    elif line.startswith("dir"):
        Directory(line.removeprefix("dir ").removesuffix(
            '\n'), parent=current_dir)
    else:
        current_dir.content_size += int(line.split(' ')[0])

dirs_under_threshold = list()

# iterate over the tree from leaves to the root
for dir in PostOrderIter(root):
    if dir is root:
        continue
    dir.parent.content_size += dir.content_size

# print the tree
for pre, _, dir in RenderTree(root):
    if dir.content_size < SIZE_THRESHOLD:
        dirs_under_threshold.append(dir)
    print("%s%s %s" % (pre, dir.name, dir.content_size))

sum = sum(dir.content_size for dir in dirs_under_threshold)

print(f"\nTOTAL SPACE:\t{FILE_SYSTEM_SIZE}")
print(f"FREE SPACE:\t{FILE_SYSTEM_SIZE - root.content_size}")
print(
    f"NEED TO REMOVE:\t{NEEDED_SPACE - (FILE_SYSTEM_SIZE - root.content_size)}")

dir_to_remove = root
SPACE_TO_REMOVE = NEEDED_SPACE - (FILE_SYSTEM_SIZE - root.content_size)

# Find the smallest dir that would free up enough space:
for dir in PreOrderIter(root):
    if dir.content_size >= SPACE_TO_REMOVE and dir.content_size < dir_to_remove.content_size:
        dir_to_remove = dir

print(
    f"FILE TO REMOVE:\t{dir_to_remove.content_size} {dir_to_remove.name}")
