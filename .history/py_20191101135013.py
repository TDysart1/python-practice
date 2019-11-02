# simple Pig latin transformer
# pyg = 'ay'
# original = input('Enter a word: ')
# if(len(original) > 0 and original.isalpha()):
#     word = original
#     first = word[0]
#     newWord = word + first + pyg
#     newWord = newWord[1:len(newWord)]
#     print(newWord)
# else:
#     print('empty')

# Guess the number
# import random
# def startGame():
#     while True:
#         gameStart = input('type y to begin')
#         if gameStart == 'Y' or 'y':
#             print(game())
#         if gameStart != 'Y' or 'y':
#             input('I said y!')
#             print(game())
# def restart():
#             startGame()
# def game():
#     guessCounter = 0
#     playerName = input('What is your name?')
#     print('Hello %s! Can you guess what number, I\'m thinking? 1 thru 5' % (playerName))
#     number = random.randint(1,5)
#     while guessCounter <= 5:
#         print('What is your guess?')
#         guessNum = int(input())
#         guessCounter = guessCounter + 1
#         if guessNum < number:
#             print('Guess too low')

#         if guessNum > number:
#             print('Guess too high')
#         if guessNum == number:
#             break
#         if guessCounter > 5:
#             number = str(number)
#             print('Wrong! Number was %s! Guess again' % (number))
#             print('You have failed to guess the number! YOU LOSE!')
#             print(restart())

#     if guessNum == number:
#             guessCounter = str(guessCounter)
#             print('You guessed the number in %s guesses!' %(guessCounter))
#             print(restart())


# startGame()


# login site
# users = {}
# status = ''

# def displayMenu():
#     status = input('Are you a registered user? y/n? Press \'q to quit')
#     if status == 'y':
#         oldUser()
#     elif status == 'n':
#         newUser()

# def newUser():
#     createLogin = input('Create login username: ')

#     if createLogin in users:
#         print('\nUsername already taken\n')
#         createLogin = input('enter new username: ')
#         createPassword = input('Create password: ')
#         users[createLogin] = createPassword
#         print('\nUser created\n')
#     else:
#         createPassword = input('Create password: ')
#         users[createLogin] = createPassword
#         print('\nUser created\n')

# def oldUser():
#     login = input('Enter login: ')
#     passw = input('Enter password: ')
#     if login in users and users[login] == passw:
#         print('\nLogin Successful\n')
#     else:
#         print('\nWrong information!\n')

# while status != 'q':
#     displayMenu()

# print(users)

# RPS

# import random
# r = 1
# p = 2
# s = 3

# def restart():
#     gameStart()

# def gameStart():
#     myscore = 0
#     computerscore = 0
#     while myscore < 5:
#         while computerscore < 5:
#             pc = int(input('\n Choose 1,2, or 3\n'))
#             cc = random.randint(1,3)
#             if pc == cc:
#                 print('draw')
#             if (pc + 1) == cc or (cc + 2) == pc:
#                 computerscore = computerscore + 1
#                 print('computer wins!')
#             if (pc + 2) == cc or (cc + 1) == pc:
#                 myscore = myscore + 1
#                 print('you win!')
#             if myscore == 5:
#                 print('You won! Score %s - %s' % (myscore,computerscore))

#                 playagain = input('Wanna play again? y/n: ')
#                 if playagain == 'y':
#                     restart()
#                 else:
#                     print('Thanks for playing!')

#             if computerscore == 5:
#                 print('You lost! Score %s - %s' % (myscore,computerscore))
#                 playagain = input('Wanna play again? y/n: ')
#                 if playagain == 'y':
#                     restart()
#                 else:
#                     print('Thanks for playing!')

# gameStart()


# Generating sin vs cosine

# import matplotlib.pyplot as plt
# import numpy as np


# Generating a password
# minimum 6 words random letters (upper and lower case)


# import random
# import string
# now lets see what this string module provide us.
# I wont be going into depth because the python
# documentation provides ample information.
# so lets generate a random string with 32 characters.

# def randomPassword():
#     createP = input('Want us to create your password? y/n ')
#     def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
# 	        return ''.join(random.choice(chars) for _ in range(size))
#     if( createP == 'y'):
#         print(pw_gen(int(input('How many characters in your password?'))))

#     if( createP == 'n'):
#         passw = input('Enter password: ')
#         while (len(passw) < 6):
#             print ('Password needs to be 6 characters!')
#             passw = input('Enter password:')
#             if(len(passw) >= 6):
#                 print('Your password is: %s' %(passw))

# randomPassword()

# def startGame():
#     while True:
#         gameStart = input('type y to begin')
#         if gameStart == 'Y' or 'y':
#             print(game())
#         if gameStart != 'Y' or 'y':
#             input('I said y!')
#             print(game())
# def restart():
#             startGame()
# def game():
#     guessCounter = 0
#     playerName = input('What is your name?')
#     print('Hello %s! Can you guess what word, I\'m thinking?' % (playerName))
#     word = random.randint(1,5)
#     while guessCounter <= 5:
#         print('What is your guess?')
#         guessNum = int(input())
#         guessCounter = guessCounter + 1
#         if guessNum < number:
#             print('Guess too low')

#         if guessNum > number:
#             print('Guess too high')
#         if guessNum == number:
#             break
#         if guessCounter > 5:
#             number = str(number)
#             print('Wrong! Number was %s! Guess again' % (number))
#             print('You have failed to guess the number! YOU LOSE!')
#             print(restart())

#     if guessNum == number:
#             guessCounter = str(guessCounter)
#             print('You guessed the number in %s guesses!' %(guessCounter))
#             print(restart())


# startGame()


friends = ['Will', 'Trei', 'Trei','Jeff']
friends.insert(1, 'Ty')
friends.sort()
print(friends)