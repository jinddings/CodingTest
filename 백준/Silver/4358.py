import sys

total_number_of_tree = 0
dict_trees = {}
while True:
    input_str = sys.stdin.readline().rstrip()
    if input_str == '':
        break
    if input_str not in dict_trees:
        dict_trees[input_str] = 1
        total_number_of_tree += 1
    else :
        dict_trees[input_str] += 1
        total_number_of_tree += 1


dict_trees = sorted(dict_trees.items())

for item in dict_trees:
    tree, count = item
    print("{} {:.4f}".format(tree,count/total_number_of_tree*100))


