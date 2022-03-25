def valid_parentheses(string):
    string = ''.join(filter(lambda l: '' if l.isalpha() else l, string))
    while '()' in string:
        string = string.replace('()','')
    return string == ''
