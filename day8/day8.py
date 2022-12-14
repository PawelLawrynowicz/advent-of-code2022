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

visible_trees = 0
scenic_score = 0

for i, line in enumerate(tree_patch):
    for j, tree in enumerate(line):
        if j == 0 or j == len(line) - 1 or i == 0 or i == len(tree_patch) - 1:
            visible_trees += 1
            continue
        else:
            neighbors = list(
                (np.flip(tree_patch[i, :j]),  # left
                 tree_patch[i, j + 1:],  # right
                 tree_patch[i+1:, j],  # bottom
                 np.flip(tree_patch[:i, j]))  # top
            )
            for side in neighbors:
                if max(side) < tree:
                    visible_trees += 1
                    break

            print(neighbors)
            side_scores = [0, 0, 0, 0]
            for side, neighbor_trees in enumerate(neighbors):
                for neighbor_tree in neighbor_trees:
                    side_scores[side] += 1
                    if neighbor_tree >= tree:
                        break
            if np.prod(side_scores) > scenic_score:
                scenic_score = np.prod(side_scores)

print(scenic_score)
