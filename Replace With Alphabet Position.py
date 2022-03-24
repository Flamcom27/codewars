def alphabet_position(text:str):        
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        'o', 'p', 'q', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y', 'z'
    ]
    text = list(text.lower())
    text = [i for i in text if i in letters]
    text = str(list(map(lambda a: letters.index(a) + 1, text)))
    for i in ('[', ']', ','):
        text = text.replace(i, '')
    return str(text)
print(alphabet_position("The sunset sets at twelve o' clock."))