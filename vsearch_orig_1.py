def search4vowels(word):
    """vsearch.py is a function that displays any vowels found
    in a word as an argument."""

    vowels = set('aeiou')

    found = vowels.intersection(set(word))
    found_list = sorted(list(found))

    print(found_list)


        
