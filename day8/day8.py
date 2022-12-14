import numpy as np

# 30373
# 25512
# 65332
# 33549
# 35390

tree_patch = open("day8/input", "r").readlines()

for i in range(len(tree_patch)):
    tree_patch[i] = np.array([int(d)
                             for d in str(tree_patch[i].replace('\n', ''))])


tree_patch = np.array(tree_patch, dtype=int)


print(tree_patch)

visible_trees = 0

# visible_trees += 2 * tree_patch_width + 2 * (tree_patch_height - 2)


for i, line in enumerate(tree_patch):
    for j, tree in enumerate(line):
        if j == 0 or j == len(line) - 1 or i == 0 or i == len(tree_patch) - 1:
            visible_trees += 1
            continue
        else:
            neighbors = list(
                (tree_patch[i, :j],
                 tree_patch[i, j + 1:],
                 tree_patch[i+1:, j],
                 tree_patch[:i, j])
            )
            for side in neighbors:
                if max(side) < tree:
                    visible_trees += 1
                    break


print(visible_trees)
