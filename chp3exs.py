
things = ['mozzarella', 'cinderella', 'salmonella']

test = things[1].capitalize()

print(test)

test = things[0].upper()

print(test)

print(things)

things.pop()

print(things)

surprise = ['Groucho', 'Chico', 'Harpo']

print(surprise)

surprise = surprise[-1].lower()

print(surprise)

surprise = surprise[::-1].capitalize()

print(surprise)

e2f = {'dog':'chien','cat':'chat','walrus':'morse'}

print(e2f)

print(e2f['walrus'])

french = []
english = []

french = e2f.values()
english = e2f.keys()

f2e = dict(zip(french,english))

print(f2e)

print(f2e['chien'])

eng_keys = set(e2f.keys())

print(eng_keys)

life = {
	'animals':{
		'cats':['Henri','Grumpy','Luci'],
		'octopi':{},
		'emus':{}
	},
	'plants':{},
	'other':{}

}

print(life.keys())

print(life['animals'].keys())

print(life['animals']['cats'])







