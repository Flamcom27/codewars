def valid_braces(string):
    my_list = []
    for i in string[:]:
        if i == '(' or i == '[' or i == '{':
            my_list.append(i)
        else:
            if len(my_list) == 0: return False
            last_value = my_list[len(my_list) - 1]
            if (i == ')' and last_value == '(') or (i == ']' and last_value == '[') or (i == '}' and last_value == '{'):
                my_list.pop()
            else:
                return False
    return len(my_list) == 0

print(valid_braces('(((({{'))