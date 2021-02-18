from random import randint

class Roulette():
	
	red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36,]
	black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35,]
	green = [0]
	spins = 0
	even_status=''
	
	#represent the roulette wheel which has 37 outcomes
	def __init__(self):
	    self.number = randint(0, 36)
	    if self.number in self.red:
	    	self.colour = "Red"
	    elif self.number in self.black:
	        self.colour = 'Black'
	    elif self.colour in self.green:
	    	self.colour = 'Green'     

	    Roulette.spins += 1

	def check_colour(self):
		if self.number in Roulette.red:
			return "Red"
		elif self.number in Roulette.black:
			return "Black"
		else:
			return "Green"

	def is_even(self):
		#check if the result was even or not, 0 is not
		if self.number == 0:
			return False
		elif self.number % 2 == 0:
			self.even_status = "Even"
			return True
		else:
			self.even_status = "Odd"
			return False

	def check_twelve(self):
		#check which twelve the number falls into
		if self.number == 0:
			return None
		elif self.number < 13:
			return 'First 12'
		elif self.number < 25:
			return 'Second 12'
		else:
			return 'Third 12'

	def print_spins():
		print('Spin no....', Roulette.spins)

	def print_is_even(self):
		if self.is_even() == True:
			self.even_status = "Even"
		elif self.is_even() == False:
			self.even_status = "Odd"
		return '{} is {}'.format(self.number, self.even_status)
