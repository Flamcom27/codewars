def spin_words(sentence):   
    return " ".join(map(lambda i: i[::-1] if len(i) >= 5 else i, [i for i in sentence.split(" ")]))
print(spin_words("This sentence is a sentence"))