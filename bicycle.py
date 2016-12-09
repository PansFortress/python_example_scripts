class Bicycle(object):
	"""docstring for Bicycle"""
	def __init__(self, model, weight, cost):
		self.model = model
		self.weight = weight
		self.cost = cost

	def printDetails(self):
		print("Model : {} \nWeight : {} \nCost : {} \
			".format(self.model, self.weight, self.cost))

class BikeStore(object):
	"""docstring for BikeStore"""
	def __init__(self, name):
		self.name = name
		self.bicycles = []

	def stockBicycle(self, model, weight, cost):
		markup_price = cost + (cost * .20)
		self.bicycles.append(Bicycle(model, weight, markup_price))

	def showBicycles(self):
		for bicycle in self.bicycles:
			bicycle.printDetails()

class Customers(object):
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

store = BikeStore("Jims")
store.stockBicycle("Trek", 124, 500)
store.showBicycles()

james = Customers("James", 1500)
james.buyBicycle(store.bicycles[0])
print(james.fund)