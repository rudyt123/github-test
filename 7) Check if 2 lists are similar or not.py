list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
count_l = 0
count_l_2 = 0
y = False
for l_1 in list_1:
    count_l += 1
for l_2 in list_2:
    count_l_2 += 1
for x in list_1:
    if x in list_2:
        y = True
        pass
    if x not in list_2:
        y = False
        break
if count_l == count_l_2 and y == True:
    print(f'{list_1} and {list_2} are similar')
if count_l != count_l_2 or y == False:
    print(f'{list_1} and {list_2} are NOT similar')
