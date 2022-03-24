def rot13(message:str)->str:
    from string import ascii_lowercase as ascii
    def func(letter:str)->str:
        if not letter.isalpha(): return letter
        print(letter)
        letter_index = ascii.index(letter.lower()) + 13
        try:
            if letter.islower(): return (ascii[letter_index])
            else: return (ascii[letter_index]).capitalize()          
        except IndexError:
            if letter.islower(): return(ascii[letter_index - 26]) 
            else: return (ascii[letter_index - 26]).capitalize() 
    return ''.join(map(func, message)) 
print(rot13('3JJjckejnfsjkej4y378^%^%$&euf04u'))
