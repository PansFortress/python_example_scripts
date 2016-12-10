import random

questions = {
	"strong": "Do you like yer drinks strong?",
	"salty": "Do you like it with a salty tang?",
	"bitter": "Are ya lubber who likes it bitter?",
	"sweet": "Would ye like a bit of sweetness with yer poison?",
	"fruity": "Are ye one for a fruity finish?",
}

ingredients = {
	"strong": ["glug of rum", "slug of whisky", "splash of gin"],
	"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
	"sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
	"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
	"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
}


def raise_questions():
	answers = {}

	acceptable = ["yes", "y"]
	for item in questions:
		holder = input(questions[item] + " ")
		if holder.lower() in acceptable:
			answers[item] = True
		else:
			answers[item] = False
	return answers

#How should i name params with same names as global variables?
def make_drink(answers):
	drink = []
	for item in answers:
		if answers[item]:
			drink.append(random.choice(ingredients[item]))
	return drink

if __name__ == "__main__":
	drink = " ".join(make_drink(raise_questions()))
	print(drink)