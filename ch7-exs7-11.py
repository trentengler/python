print('Ex 7-7')

print()
mammoth = """We have seen the queen of cheese, 
Laying quietly at your ease, 
Gently fanned by evening breeze, 
Thy fair form no flies dare seize. 

All gaily dressed soon you'll go 
To the great Provincial Show, 
To be admired by many a beau 
In the city of Toronto. 

Cows numerous as a swarm of bees, 
Or as the leaves upon the trees, 
It did require to make thee please, 
And stand unrivalled, queen of cheese. 

May you not receive a scar as 
We have heard that Mr. Harris 
Intends to send you off as far as 
The great world's show at Paris. 

Of the youth beware of these, 
For some of them might rudely squeeze 
And bite your cheek, then songs or glees 
We could not sing oh! queen of cheese. 

We'rt thou suspended from baloon, 
You'd cast a shade even at noon; 
Folks would think it was the moon 
About to fall and crush them soon."""
print()
print(mammoth)
print()
print()
print('Ex 7-8 ... Find all words that begin with c')
print()

import re

print(re.findall(r'\b[C|c]\w*',mammoth))

print()
print()
print('Ex 7-9 ... Find all 4 letter words that begin with c')
print()

print(re.findall(r'\b[C|c]\w{3}\b',mammoth))
print()
print()
print('Ex 7-10 ... Find all words that end with r')
print()
print(re.findall(r'\b\w*[R|r]\b',mammoth))
print()
print()
print('Ex 7-11 ... Find all words that have 3 consecutive vowels')
print()

print(re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b',mammoth))
print()

