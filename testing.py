
# 4) Merge Two Lists and Sort it

list_1 = [1, 2, 6]
list_2 = [3, 5, 4]
merged_list = list_1 + list_2
largest_int = 0
sort_list = []

for big in merged_list:
    if big > largest_int:
        largest_int = big

smallest = merged_list[0]
for items in merged_list:
    if items < smallest:
        smallest = items

sort_list.insert(0, largest_int)
sort_list[0] = largest_int
sort_list.append(smallest)
sort_list[-1] = smallest
merged_list.remove(smallest)
merged_list.remove(largest_int)
y = smallest

for x in merged_list:
    if x > y:
        sort_list.insert(1, x)
    if x < y:
        sort_list.insert(2, x)
    y = x
print(sort_list)
