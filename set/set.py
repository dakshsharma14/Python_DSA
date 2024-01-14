# unordered collection
my_set = {1, 2, 3, 4, 5, 6, 6}
your_set = {4, 6, 7, 1, 5, 9, 3}
my_set.add(34)
print(my_set)
print(1 in my_set)

# we have a list, we want to return something with
# no duplicates
my_list = [2, 4, 5, 5, 6, 7, 9]
print(set(my_list))

mine_set = {1, 2, 3, 4, 5, 6, 6, 9}
your_set = {4, 6, 7, 1, 5, 3}

# print(mine_set.difference(your_set))
# print(mine_set.discard(9))
# # print(mine_set)
# print(mine_set.difference_update(your_set))
# print(mine_set)

print(mine_set.isdisjoint(your_set))
print(mine_set.union(your_set))
print(mine_set.issubset(your_set))
