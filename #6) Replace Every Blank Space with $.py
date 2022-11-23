example_str = 'hello world !'
result_str = ''
for x in example_str:
    if x == ' ':
        x = '$'
    result_str += x
print(result_str)
