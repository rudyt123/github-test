#3) Find vowels in String "Python is wonderful language. Python is a good gateway language for beginners."
result_str = ''
vowels_list = ['a','i','e','o','u']
for vowel in "Python is wonderful language. Python is a good gateway language for beginners.":
    for alpha in vowels_list:
        if vowel == alpha:
            result_str += alpha
print (result_str)