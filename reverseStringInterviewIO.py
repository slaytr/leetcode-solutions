import string

in_list = ['p', 'a', 'c', ' ', 'c', 'p', 'a', ' ']

def reverse(char_list):
    res = []
    temp_res = []
    for value in char_list:
        if value in string.ascii_lowercase:
            temp_res.append(value)
        else:
            res = [value] + temp_res + res
            temp_res = []
    return temp_res + res

print(reverse(in_list))