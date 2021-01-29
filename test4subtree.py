import numpy as np

class Dog:
	"""it's a dog"""
	def __init__(self, name, age, length):
		self.name = name
		self.age = age
		self.length = length

	def sit(self):
		print(f"a {self.age} dog named {self.name} is sitting down")

jack = Dog('jack', 8)
jack.sit()		