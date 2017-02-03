
print('Exercise 6-1')
print()
class Thing():
	pass

print(Thing)

print()
example = Thing()

print(example)

print()

print('Exercise 6-2')

class Thing2():
	letters = 'abc'

print()
print(Thing2.letters)

print()

print('Exercise 6-3')

class Thing3():
	def __init__(self):
		self.letters = 'xyz'

print()

uglyThing = Thing3()

print()

print(uglyThing.letters)

print()

print('Exercise 6-4')

class Element():
	def __init__(self, name, symbol, number):
		self.hidden_name = name
		self.hidden_symbol = symbol
		self.hidden_number = number
	@property
	def name(self):
		return  self.hidden_name
	@property
	def symbol(self):
		return self.hidden_symbol
	@property
	def number(self):
		return self.hidden_number
	def __str__(self):
		return('name=%s, symbol=%s, number=%s' %(self.name,self.symbol,self.number))

hydrogen = Element('Hydrogen','H','1')

print()
# print(hydrogen.name)
# print(hydrogen.symbol)
# print(hydrogen.number)
print()

print()

print('Exercise 6-5')

print()
hydro={'name':'Hydrogen','symbol':'H','number':'1'}

hydro
print(hydro)
print(hydro.values())
print()

h1 = Element(**hydro)
#h1 = Element(hydro['name'],hydro['symbol'],hydro['number'])
print(h1)
print()

print('Exercise 6-6')
print()
print(h1)
print()

print()
print('Exercise 6-7')
print()
h2 = Element(**hydro)
print(hydrogen)
print(h2)


print()
print('Exercise 6-8')
print()

h3 = Element(**hydro)
print(h3)
print(h3.name)
print(h3.symbol)
print(h3.number)

print()
print('Exercise 6-9')
print()




