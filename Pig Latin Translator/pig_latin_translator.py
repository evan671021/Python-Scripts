while True:
    vowels = ['a','e','i','o','u']
    word = input('Enter a word.')
    first = word[0]
    if first in vowels:
        answer = word + 'ay'
    elif word == 'quit':
        break
    else:
        answer = word[1:] + first + 'ay'

    print(answer)
