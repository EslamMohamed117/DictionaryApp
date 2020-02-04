import json
data = json.load(open("data.json"))
def key_to_def(word):
	word = word.lower()
	g="" 
	if data.get(word):
		a = ""
		answer = data.get(word)
		for i in answer:
			a += i + "\n"
		return a
	else:
		for q in word:
			g+=q
			if g in data:
				t = "Did you mean %s ? (y or n)" % g
				if input(t) == "y":
					return key_to_def(g)
		return "Error 404 not found"
print(key_to_def(input("Please enter: ")))

