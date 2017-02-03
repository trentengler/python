

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join(plist[-7:-9:-1])
new_phrase = new_phrase + ''.join(plist[-5:-7:-1])
                                      
print(plist)
print(new_phrase)


