

def search4vowels(phrase:str)-> set:
    """Returns any vowels found in a phrase supplied as an argument."""

    vowels = set('aeiou')

    return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str='aeiou')-> set:
    """Returns any letters (or vowels by default) found in a phrase
    supplied as an argument."""

    return set(letters).intersection(set(phrase))


        
