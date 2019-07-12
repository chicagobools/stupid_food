import itertools
import random
import pyttsx
import sys

class Fooder:
	def __init__(self, food):
		self.food = food.split()

		with open('dict.txt') as f:
			self.words = [word.strip() for word in f]

	def hamming_distance(self, this, that):
		distance = 0
		if len(this) != len(that):
			return -1
		if this == that:
			return len(that)
		for a,b in zip(this, that):
			if a == b:
				distance += 1
		return distance

	def compare_hamm(self, this):
		return [word for word in self.words if self.hamming_distance(this, word) > len(this)/2]

	def close_food(self, count=1):
		t = [self.compare_hamm(word) for word in self.food]
		for i in range(count):
			yield [random.choice(l) for l in t]




obj = Fooder(' '.join(sys.argv[1:]))

foods = list(obj.close_food(10))

conc = [' '.join(f) for f in foods]

engine = pyttsx.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-72)

for word in conc[:4]:
	print word
	sys.stdout.flush()
	engine.say(word)

engine.runAndWait()

