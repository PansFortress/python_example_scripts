from bicycle import *

if __name__ == "__main__":
	store = BikeStore("Jims")

	store.stockBicycle("Trek", 124, 100)
	store.stockBicycle("Giant", 140, 400)
	store.stockBicycle("Hurley", 150, 900)
	store.stockBicycle("Trek2", 190, 200)
	store.stockBicycle("Giant2", 150, 300)

	james = Customer("James", 200)
	sarah = Customer("Sarah", 500)
	carl = Customer("Carl", 1000)

	sellBike(store, james)
	sellBike(store, sarah)
	sellBike(store, carl)

	print("CUSTOMER DETAILS")
	james.showStuff();
	print("STORE DETAILS")
	store.showBicycles();