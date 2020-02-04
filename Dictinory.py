import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def key_to_def(word):
	word = word.lower() 
	if data.get(word):
		a = ""
		answer = data.get(word)
		for i in answer:
			a += i + "\n"
		return a
	elif len(get_close_matches(word,data.keys())) > 0:
		h = input("Did you mean %s instead? (y or n)" % get_close_matches(word,data.keys())[0])
		if h == "y":
			return key_to_def(get_close_matches(word,data.keys())[0])
		elif h == "n":
			return "Error 404 not found"
		else:
			return "Sorry we couldn`t understand your answer, please try again"
	else:
		return "Error 404 not found"
print(key_to_def(input("Please enter: ")))


#g=""
		#for q in word:
			#g+=q
			#if g in data:
				#t = "Did you mean %s ? (y or n)" % g
				#if input(t) == "y":
					#return key_to_def(g)
