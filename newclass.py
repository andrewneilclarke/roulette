import random

class Roulette():
	def __init__(self, numbers):
		numbers = {(1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36): 'Red',
				(2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35): 'Black',
				0: 'Green',
				}

		self.result = result
		
	def rollball():
		result = random.randint(0, 35)

		return result
	
	def check_odd_even(result):
		""" check if the result was odd or even and return the result """
		odd = False
		even = False
		if result % 2 == 0:
			even = True
		else:
			odd = True
		return odd, even

	def check_colour():
		if result in numbers[0]:
			numbers[0] = True
		elif result in numbers[1]:
			numbers[1] = True
		else:
			numbers[2] 
		return numbers[0, 1, 2]
	rollball()

print(Roulette.check_odd_even(14))
#print(Roulette.check_colour())
#Draw = Roulette(9)
#print(Roulette.rollball(result))
