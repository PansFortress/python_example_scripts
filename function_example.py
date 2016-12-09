def side_effect_test(value):
	value += ("orange","Green")
	print("Inside the function, the value become {}".format(value))

if __name__ == "__main__":
	value = ("green","Blue")

	print("Outside the function, the value starts as {}".format(value))

	side_effect_test(value);

	print("Outside t he function, th e value is now {}".format(value))