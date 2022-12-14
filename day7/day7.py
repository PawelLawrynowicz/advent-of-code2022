from anytree import NodeMixin, Node, find, RenderTree, PostOrderIter

SIZE_THRESHOLD = 100_000
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
for pre, _, node in RenderTree(root):
    if node.content_size < SIZE_THRESHOLD:
        dirs_under_threshold.append(node)
    print("%s%s %s" % (pre, node.name, node.content_size))

sum = sum(dir.content_size for dir in dirs_under_threshold)


print(sum)
