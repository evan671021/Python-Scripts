from random import randint
while True:
    question = input('What is your question? ')
    if question == 'quit':
        break
    num = randint(1,20)
    if num == 1:
        print("As I see it, yes.")
    elif num == 2:
        print("Ask again later.")
    elif num == 3:
        print("Better not tell you now.")
    elif num == 4:
        print("Cannot predict now.")
    elif num == 5:
        print("Concentrate and ask again.")
    elif num == 6:
        print("Don’t count on it.")
    elif num == 7:
        print("It is certain.")
    elif num == 8:
        print("It is decidedly so.")
    elif num == 9:
        print("Most likely.")
    elif num == 10:
        print("My reply is no.")
    elif num == 11:
        print("My sources say no.")
    elif num == 12:
        print("Outlook not so good.")
    elif num == 13:
        print("Outlook good.")
    elif num == 14:
        print("Reply hazy, try again.")
    elif num == 15:
        print("Signs point to yes.")
    elif num == 16:
        print("Very doubtful.")
    elif num == 17:
        print("Without a doubt.")
    elif num == 18:
        print("Yes.")
    elif num == 19:
        print("Yes – definitely.")
    elif num == 20:
        print("You may rely on it.")
