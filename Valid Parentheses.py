from re import L


def valid_parentheses(string):
    string = ''.join(filter(lambda l: '' if l.isalpha() else l, string))
    while '()' in string:
        string = string.replace('()','')
    return string == ''
    return list(map(lambda string: string.replace('()', ''), string))
print(valid_parentheses('r(tinzce(z)wksfov)'))#true
