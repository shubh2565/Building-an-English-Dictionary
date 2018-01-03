# a simple dictionary which ask the user to enter a word and dispaly it's meaning


import json

data = json.load(open('data.json'))

def find_meaning(word):
    
    return data[word]


word = input('Enter a word : ')
print(find_meaning(word))

choice = input('Want to enter again? y for yes and n for no :')

while(choice is 'y'):
    word = input('Enter a word : ')
    print(find_meaning(word))
    choice = input('Want to enter again? y for yes and n for no :')


