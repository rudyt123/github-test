# 2) Find odd and even numbers in 5 to 100
for nums in range(5, 100 + 1):
    if nums % 2 == 0:
        print(f' {nums} is even')
    else:
        print (f' {nums} is odd')