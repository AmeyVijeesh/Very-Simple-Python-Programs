import random

print("""Hello!
Welcome to the guessing game!
If you get the correct answer, you win!
If you lose, you have to pay!""")


guess = int(input("""Enter a number between one(1) and hundred (100) 
"""))
if 1 <= guess <= 100:
    outcome = random.randint(1, 100)
    if guess == outcome:
        print("You have guessed it right! The answer is", outcome)
    else:
        print("Sorry,the answer is not", guess, "!" "It is ", outcome, "!", "Better luck next time!")

else:
    print("Please enter a number between 1 and 10-")
print("Thank you!")
