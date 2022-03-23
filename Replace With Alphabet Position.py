def alphabet_position(text:str):        
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        'o', 'p', 'q', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y', 'z'
    ]
    text = list(text.lower())
    text = [i for i in text if i in letters]
    text = map(lambda a: letters.index(a) + 1, text)
    text = str(list(text))
    for i in ('[', ']', ','):
        text = text.replace(i, '')
    # for i in text:
        # if i in letters:
        #     num = letters.index(i) + 1
        #     text = text.replace(i, f'{num}')
    #     elif i == ' ':
    #         continue
    #     else:
    #         text = text.replace(i, '')
    return str(text)
print(alphabet_position("The sunset sets at twelve o' clock."))