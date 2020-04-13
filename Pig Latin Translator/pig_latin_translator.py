vowels = ['a','e','i','o','u']
word = input('Enter a word.')
first = word[0]
if first in vowels:
    letters = []
    letters.append(list(word))
    letters.append('a''y')
    
print(letters)
