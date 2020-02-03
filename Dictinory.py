import json
data = json.load(open("data.json"))
def key_to_def(word):
	word = word.lower()
	q=""
	for q in word:
		if q in data:
			if input("Did you mean %s ?" % q) == y)
				word = q		
	if data.get(word):
		a = ""
		answer = data.get(word)
		for i in answer:
			a += i + "\n"
		return a
	else:
		return "Error 404 not found"
print(key_to_def(input("Please enter: ")))

