

vowels = set('aeiou')

word = input("Provide a word to search for vowels: ")

i = vowels.intersection(set(word))
i_list = sorted(list(i))

print(i_list)


        
