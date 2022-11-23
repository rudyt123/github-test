result_str = ''
for letter_a in "Python is wonderful language. Python is a good gateway language for beginners.":
    if letter_a.lower() == 'a':
        letter_a = '$'
    result_str += letter_a
print(result_str)
