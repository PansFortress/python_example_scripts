import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at runtime".format(len(sys.argv)))

for arg in sys.argv:
	print(arg)