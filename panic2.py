

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

ontap = []
ontap.append(plist.pop(1))
ontap.append(plist.pop(1))
ontap.append(plist.pop(3))
ontap.append(plist.pop(2))
ontap.append(plist.pop(3))
ontap.append(plist.pop(2))

print(ontap)

new_phrase = ''.join(ontap)
print(plist)
print(new_phrase)


