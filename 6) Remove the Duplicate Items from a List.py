list_1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 3, 4, 5, 6]
new_list = []
for x in list_1:
    if x not in new_list:
        new_list.append(x)
    if x in new_list:
        pass
print(new_list)
