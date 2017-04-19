import random

class Employee(object):   n 1	11		`8  

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def __str__(self):
		return 'employee name: {} {}'.format(self.first_name, self.last_name)

	def eat(self, food=None, companions=None):
		self.food = food
		self.companions = companions
		restaurants = [ 'Taco Bell', 'Smokin Thighs', 'City House', 'Rolf and Daughters', 'Five Points Pizza', 'Miel', 'Margot', 'Provence']
		random_restaurant = random.choice(restaurants)

		if food is None and companions is None:
			print('{} {} ate at {}'.format(self.first_name, self.last_name, random_restaurant))
		elif food is not None and companions is None:
			print('{} {} ate a {} in the Snackery'.format(self.first_name, self.last_name, food))
		elif food is None and companions is not None:
			print('{} {} ate at {} with {}'.format(self.first_name, self.last_name, random_restaraunt, ', '.join(companions)))
		elif food is not None and companions is not None:
			print('{} {} ate at {} and ordered {} with {}.'.format(self.first_name, self.last_name, random_restaurant, food, ', '.join(companions)))


class FullTime(object):
	def __init__(self):
		self.hours_per_week = 40

class PartTime(object):
	def __init__(self):
		self.hours_per_week = 24




