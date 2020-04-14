x = None

def letter_caps(x):
    while True:
        answer = []
        x = input("Type a sentence. ")
        if x == 'quit':
            break
        for letter in range(len(x)):
            if letter%2 == 0:
                answer.append(x[letter].lower())
            else:
                answer.append(x[letter].upper())
        print(''.join(answer))

letter_caps(x)
