import json
from difflib import get_close_matches
import time

data = json.load(open("data.json"))

def find_word(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(word, data.keys())[0])
        if yn.upper() == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.upper() == "N":
            return "The word does not exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "That word does not exist. Please double check it."

while True:
    word = input("\nEnter a word. ")

    if word == 'exit dictionary':
        break
    else:
        output = find_word(word)

    if type(output) == list:
        for item in output:
            print('\n', item)

    else:
        print(output)

    time.sleep(3)
