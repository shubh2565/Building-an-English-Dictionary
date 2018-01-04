import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def find_meaning(w):

	w = w.lower()

	if w in data:
		return data[w]

	elif w.title() in data:
		return data[w.title()]

	elif w.upper() in data:
		return data[w.upper()]

	elif len(get_close_matches(w, data.keys(), cutoff=0.7)) > 0:
		yn = input("Did you mean %s instead? " % get_close_matches(w, data.keys())[0])
		if yn is 'y':
			return data[get_close_matches(w, data.keys())[0]]
		else:
			return "We didn't understand your entery"

	else:
		return "This word does't exist"


choice = 'y'

while(choice is 'y'):

    word = input('Enter a word : ')
    output = (find_meaning(word))

    if type(output) is list:
    	for item in output:
    		print(item)

    else:
    	print(output)

    choice = input('Want to enter again? y for yes and n for no :')


