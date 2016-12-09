import sys

script_input = sys.argv[1]

for i in range(0, int(script_input)):
	if (i == 0):
		print(0)
	elif(i % 15 == 0):
		print("fizzbuzz")
	elif(i % 3 == 0):
		print("fizz")
	elif(i % 5 == 0):
		print("buzz")
	else:
		print(i)
