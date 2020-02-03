import json
data = json.load(open("data.json"))
def key_to_def(word):
	word = word.lower()
	q="" 
	if data.get(word):
		a = ""
		answer = data.get(word)
		for i in answer:
			a += i + "\n"
		return a
	else:
		for q in word:
			if q in data:
				t = "Did you mean %s ?" % q
				print(t)
				if input(t) == "y":
					return key_to_def(q)
                        	else:
                                	q+=q
			else:
				q+=q
			return "Error 404 not found"
print(key_to_def(input("Please enter: ")))

