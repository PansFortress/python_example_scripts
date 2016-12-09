class Musician(object):
	def __init__(self, sounds):
		self.sounds = sounds

	def solo(self,length):
		for i in range(length):
			print(self.sounds[i % len(self.sounds)], end= " ")
		print()

class Bassist(Musician):
	def __init__(self):
		#super() calls the parent class's __init__
		super().__init__(["Twang", "Thrumb", "Bling"])

	def solo(self):
		super().solo(2);

class Guitarist(Musician):
	def __init__(self):
		super().__init__(["Boink", "Bow", "Boom"])

	def tune(self):
		print("Hey there, we've tuned ourselves to {}".format(self.sounds))

if __name__ == "__main__":
	new_bass = Bassist()
	new_guitarist = Guitarist()
	new_guitarist.tune()