import random

class Bicycle(object):
	"""docstring for Bicycle"""
	def __init__(self, model, weight, cost):
		self.model = model
		self.weight = weight
		self.cost = cost

	def printDetails(self):
		print("Model : {} \nWeight : {} \nCost : {} \n\
			".format(self.model, self.weight, self.cost))

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
		if len(self.bicycles) > 0:
			print("THESE ARE THE BIKES IN THE STORE: ")
			for bicycle in self.bicycles:
				bicycle.printDetails()
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
		self.bicycle = object

	def buyBicycle(self, bicycle):
		if self.fund > bicycle.cost:
			self.bicycle = bicycle
			self.fund -= bicycle.cost
		else:
			pass

	def showStuff(self):
		print("name: {} \nfund : {}\nbicycle : {}\n".format(self.name, 
			self.fund, self.bicycle.model))

def sellBike(store, customer):
	potential_bike = []
	for bike in store.bicycles:
		if bike.cost <= customer.fund:
			potential_bike.append(bike)

#Can I do this better?
	print("{} can afford these bikes: {}\n".format(customer.name, 
		potential_bike))

	if len(potential_bike) > 0:
		bikeToPurchase = random.choice(potential_bike)
		store.sellBicycle(bikeToPurchase)
		customer.buyBicycle(bikeToPurchase)
	else:
		print("No Bikes to Sell to {}".format(customer.name))


