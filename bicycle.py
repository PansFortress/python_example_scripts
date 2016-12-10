import random

class Bicycle(object):
	"""docstring for Bicycle"""
	def __init__(self, model, weight, cost):
		self.model = model
		self.weight = weight
		self.cost = cost

	def __repr__(self):
		return("Model : {} Weight : {} Cost : {}"
			.format(self.model, self.weight, self.cost))

class BikeStore(object):
	"""docstring for BikeStore"""
	def __init__(self, name):
		self.name = name
		self.bicycles = []
		self.profit = 0

	def stockBicycle(self, model, weight, cost):
		markup_price = cost + (cost * .20)
		self.bicycles.append(Bicycle(model, weight, markup_price))

	def showBicycles(self):
		if self.bicycles:
			for bicycle in self.bicycles:
				print(bicycle)
		else:
			print("No bicycles in stock")

	def sellBicycle(self, bicycle):
		self.profit += (bicycle.cost/6)
		self.bicycles.remove(bicycle)

class Customer(object):
	"""docstring for Customers"""
	def __init__(self, name, fund):
		self.name = name
		self.fund = fund
		self.bicycle = None

	def buyBicycle(self, bicycle):
		if self.fund > bicycle.cost:
			self.bicycle = bicycle
			self.fund -= bicycle.cost


	def showStuff(self):
		print("name: {} \nfund : {}\nbicycle : {}\n".format(self.name, 
			self.fund, self.bicycle.model))

def sellBike(store, customer):
	potential_bikes = []
	for bike in store.bicycles:
		if bike.cost <= customer.fund:
			potential_bikes.append(bike)

#Can I do this better?
	print("{} can afford these bikes: {}\n".format(customer.name, 
		potential_bikes))

	if potential_bikes:
		bikeToPurchase = random.choice(potential_bikes)
		store.sellBicycle(bikeToPurchase)
		customer.buyBicycle(bikeToPurchase)
	else:
		print("No Bikes to Sell to {}".format(customer.name))

