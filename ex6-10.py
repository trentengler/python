
class Laser():
	def does(self):
		return 'disintegrate'

class Claw():
	def does(self):
		return 'crush'

class SmartPhone():
	def does(self):
		return 'ring'


class Robot():
	def __init__(self):
		self.laser = Laser()
		self.claw = Claw()
		self.smartphone = SmartPhone()
	def does(self):
		return('I have many components: my laser, to %s, my claw, to %s, my smartphone, to %s' %(self.laser.does(),self.claw.does(),self.smartphone.does())) 

sonnie = Robot()
print(sonnie.does())



