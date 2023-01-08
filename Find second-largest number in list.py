
# to find second largest int in a list
list_1 = [10,7,4,1,0,1]
emt_list = []
largest = list_1[0]
for x in list_1:
    if x > largest:
        largest = x 
    else:
        pass
list_1.remove(largest)
largest = list_1[0]
for x in list_1:
    if x > largest:
        largest = x 
print(largest)