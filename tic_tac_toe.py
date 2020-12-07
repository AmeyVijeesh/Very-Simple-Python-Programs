import time

print("""Hello!
You are in the game of tic-tac-toe game made by Amey.""")

time.sleep(2)

name = input("Please enter first player's name- ")
name1 = input("Please enter the second player's name- ")

time.sleep(3)

print("Hello",  name.capitalize(), 'and', name1.capitalize())

time.sleep(3)

print("""In this game, use the numbers as follows-
7   8   9
4   5   6
1   2   3
It means, if you want to mark the place of 7, type 7 and so on....""")
time.sleep(4)
name_list = [name1, name]

print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print("start!")
time.sleep(1)


# Implementation of Two Player Tic-Tac-Toe game in Python.


board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in board:
    board_keys.append(key)


def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printboard(board)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ': # across the top
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['1'] == board['2'] == board['3'] != ' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['1'] == board['4'] == board['7'] != ' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['2'] == board['5'] == board['8'] != ' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['3'] == board['6'] == board['9'] != ' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['7'] == board['5'] == board['3'] != ' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board['1'] == board['5'] == board['9'] != ' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        # If neither X nor O wins and the board is full, declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart.upper() == 'Y':
        for key in board_keys:
            board[key] = " "

    elif restart.upper() == 'N':
        print("Thank you!")

    else:
        print("The game has ended.")

        game()


if __name__ == "__main__":
    game()


