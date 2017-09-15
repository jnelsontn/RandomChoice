from random import randint
import sys

class NoFileSpecified(Exception):
	pass

class GenerateRandomChoice:

	def __init__(self):
		self.file = open(sys.argv[1], 'r')
		self.contents_list = [ each_line.rstrip() for each_line in self.file ]

	def generate_random_choice(self):
		return self.contents_list[ randint(0, len(self.contents_list)-1) ]

if __name__ == '__main__':
	if len(sys.argv) is not 2:
		raise NoFileSpecified('choose a single file as an argument')

	choice = GenerateRandomChoice().generate_random_choice()
	print('randomly selected:\n{}'.format(choice))
