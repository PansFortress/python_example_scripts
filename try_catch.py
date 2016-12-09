dict_example = {
	"this" : "that",
	"fireballs": "wizards"
}

try:
	dict_example["that"]
except KeyError:
	print(KeyError)