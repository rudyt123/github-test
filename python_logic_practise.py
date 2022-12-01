# "How can mirrors be real if our eyes aren't real"

not_js = "How can mirrors be real if our eyes aren't real"
empty_list = [' ']
new_list = []
js_case = ''
for char in not_js:
    char_up = char.upper()
    char_low = char.lower()
    if empty_list[-1] == " ":
        empty_list += char_up
    if empty_list[-1] != char_up:
        empty_list += char_low
empty_list.remove(' ')
        
for vals in empty_list:
    js_case += vals
print(js_case)