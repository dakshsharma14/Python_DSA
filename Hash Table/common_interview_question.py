# def item_in_common(list1, list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return True
#     return False
#
#
# list1 = [1, 2, 5]
# list2 = [2, 4, 5]
# print(item_in_common(list1, list2))
def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    # to get the key it is O(n)
    for j in list2:
        if j in my_dict:
            return True

    return False


list1 = [1, 2, 5]
list2 = [9, 4, 6]

print(item_in_common(list1, list2))