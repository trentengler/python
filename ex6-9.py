

class Bear():
	def __init__(self,name):
		self.name = name
		self.eats = 'berries'

class Rabbit():
	def __init__(self,name):
		self.name = name
		self.eats = 'clover'	

class Octothorpe():
	def __init__(self,name):
		self.name = name
		self.eats = 'campers'

b1 = Bear('BigBear')
print()
print(b1.name)
print(b1.eats)
print()
r1 = Rabbit('CottonTail')
print()
print(r1.name)
print(r1.eats)
print()
o1 = Octothorpe('UglyO')
print()
print(o1.name)
print(o1.eats)
print()

