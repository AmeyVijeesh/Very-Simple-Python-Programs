import random
import time
print("""Hello!
Welcome to the hangman program Amey made""")
time.sleep(1)
print("To begin with.....")    

fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple', 'orange', 'grapefruit', 'avocado', 'papaya']
animals = ['cheetah', 'lion', 'tiger', 'hippopotamus', 'zebra', 'jackal', 'rhinoceros', 'elephant', 'leopard']
birds = ['sparrow', 'kingfisher', 'eagle', 'pigeon', 'owl', 'parrot', 'hummingbird', 'penguins', 'woodpecker']
flowers = ['rose', 'chrysanthemum', 'marigold', 'jasmine', 'lotus', 'tulip', 'daffodil', 'flamingo', 'daisy']
tough = ['yummy', 'zigzag', 'jazz', 'handkerchief', 'jackpot', 'lucky', 'buzzing', 'kilobyte', 'funny']
userGuesslist = []
userGuesses = []
playGame = True
category = ""
continueGame = "Y"

time.sleep(1)
name = input("Enter your name- ")
print("Hello", name.capitalize(), "let's start playing Hangman!")
time.sleep(1)
print("The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(2)
print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
time.sleep(3)
print("Let's play!")
time.sleep(1)

while True:
    while True:
        if category.upper() == 'A':
            secretWord = random.choice(animals)
            break
        elif category.upper() == 'F':
            secretWord = random.choice(fruits)
            break
        elif category.upper() == 'B':
            secretWord = random.choice(birds)
            break
        elif category.upper() == 'L':
            secretWord = random.choice(flowers)
            break
        elif category.upper() == 'T':
            secretWord = random.choice(tough)
            break

        else:
            category = input("""Please select a valid category: 
            F for Fruits 
            A for animals
            B for birds
            L for Flowers
            T for tough words
            X to exit
            """)

        if category.upper() == 'X':
            print("Bye. See you next time!")
            playGame = False
            break

    if playGame:
        secretWordList = list(secretWord)
        attempts = (len(secretWord) + 2)

        def print_guessed_letter():
            print("Your Secret word is: " + ''.join(userGuesslist))


        for n in secretWordList:
            userGuesslist.append('_')
        print_guessed_letter()

        print("The number of allowed guesses for this word is:", attempts)

        while True:

            print("Guess a letter:")
            letter = input()

            if letter in userGuesses:
                print("You already guessed this letter, try something else.")

            else:
                attempts -= 1
                userGuesses.append(letter)
                if letter in secretWordList:
                    print("Nice guess!")
                    if attempts > 0:
                        print("You have ", attempts, 'guess left!')
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            letterIndex = i
                            userGuesslist[letterIndex] = letter.upper()
                    print_guessed_letter()

                else:
                    print("Oops! Try again.")
                    if attempts > 0:
                        print("You have ", attempts, 'guess left!')
                    print_guessed_letter()

            joinedList = ''.join(userGuesslist)
            if joinedList.upper() == secretWord.upper():
                print("Wow! you won.")
                break
            elif attempts == 0:
                print("Too many Guesses!, Sorry better luck next time.")
                print("The secret word was: " + secretWord.upper())
                break

        continueGame = input("Do you want to play again? Y to continue, any other key to quit")
        if continueGame.upper() == 'Y':
            category = input("""Please select a valid category: 
            F for Fruits 
            A for Animals
            B for Birds
            L for Flowers
            T for tough words""")
            userGuesslist = []
            userGuesses = []
            playGame = True
        else:
            print("Thank You for playing. See you next time!")
            break
    else:
        break
