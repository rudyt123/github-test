
# this loop is used to find the largest value and set it as largest
for no in list_1:
    if no > Largest:
        Largest = no
Lrgst_determine.append(Largest)
Largest = Lrgst_determine[0]

# this loop is used to remove the largest int from new list
for no in list_1:
    l_2nd_help.append(no)
    if Largest in l_2nd_help:
        l_2nd_help.remove(Largest)

for no_ in l_2nd_help:
    if no_ > second_largest:
        second_largest = no_

print(second_largest)
