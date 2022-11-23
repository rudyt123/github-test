print('anagram checker')
str_1 = input('1) ')
str_2 = input('2) ')
str_1_no = 0
str_2_no = 0
for x in str_2:
    if x.lower() in str_1.lower():
        str_2_no += 1
        str_1_no = 1
    else:
        str_1_no = 1
if str_1_no == str_2_no:
    print(f' {str_1} and {str_2} are anagrams')
else:
    print (f'{str_1} and {str_2} are NOT anagrams')