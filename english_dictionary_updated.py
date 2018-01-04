import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def find_meaning(w):

	w = w.lower()

	if w in data:
		return data[w]

	elif w.title() in data:
		return data[w.title()]

	elif w.upper() in data:              # checks for acronyms
		return data[w.upper()]

	elif len(get_close_matches(w, data.keys(), cutoff=0.7)) > 0:    # cutoff value can be changed to get the desired accuracy
		yn = input("Did you mean %s instead? " % get_close_matches(w, data.keys())[0])  # [0] is used to give the best match (by default n=3)
		if yn is 'y':
			return data[get_close_matches(w, data.keys())[0]]
		else:
			return "We didn't understand your entery"

	else:
		return "This word does't exist"

# to enter as many times as the user desires
choice = 'y'

while(choice is 'y'):

    word = input('Enter a word : ')
    output = (find_meaning(word))

    if type(output) is list:     # if more than one definition is present
    	for item in output:
    		print(item)

    else:
    	print(output)

    choice = input('Want to enter again? y for yes and n for no :')


