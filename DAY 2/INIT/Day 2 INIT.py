from PIL import Image
import random
end = 30

def displayBoard():
   img=Image.open(r"IMAGE.png")
   # To view the image, we need to call the show() function in Image module
   img.show()

def play():
    # taking players names as input
    p1_name = input("Player1: Enter your name:")
    p2_name = input("Player2: Enter your name:")
    # Setting the initial scores of players and number of turns to zero
    # player1 score pp1=0
    pp1 = 0
    # player2 score pp2=0
    pp2 = 0
    # number of turns turn=0
    turn = 0
    while(1):
        # if the number of turns is even, it's player1's turn
        if turn % 2 == 0:
            print(p1_name, ": It's your turn")
            # asking player1 if he wants to continue or quit
            c = int(input("Press 1 to Continue & 0 to Quit: "))
            # Displaying scores and a thank you message if he wants to quit
            if(c==0):
                print(p1_name,': You scored ', pp1)
                print(p2_name,': You scored ', pp2)
                if(pp1 > pp2):
                    print(p1_name, " is leading by ", (pp1-pp2), " points.")
                else:
                    print(p2_name, " is leading by ", (pp2-pp1), " points.")
                    print("Thanks for playing.")
                    break
            # else, the program generates a random number from 1 to 6
            # representing a dice is rolled, using randint() function
            dice = random.randint(1,6)
            print("Dice showed: ", dice)
            # adding the dice points to the player1's score
            pp1 = pp1+dice
            # checking if there is any ladder at the player1's position
            pp1 = checkLadder(pp1)
            # checking if there is any snake at the player1's position
            pp1 = checkSnake(pp1)
            # if the player1's score is exceeding the maximum number on the board,
            # set it to maximum
            if pp1 > end:
                pp1 = end
            print(p1_name, " : Your score is ", pp1)
            if(reachedEnd(pp1)):
                print(p1_name, " won by ", (pp1-pp2), " points")
                print("Congratulations!! ", p1_name)
                print("Thanks for playing.")
                break
        else:
            # if the number of turns is odd, it's player2's turn
            print(p2_name, ": It's your turn")
            # asking player2 if he wants to continue or quit
            c = int(input("Press 1 to Continue & 0 to Quit: "))
            # Displaying scores and a thank you message if he wants to quit
            if(c == 0):
                print(p1_name, ': You scored ', pp1)
                print(p2_name, ': You scored ', pp2)
                if(pp1 > pp2):
                    print(p1_name, " is leading by ", (pp1-pp2), " points.")
                else:
                    print(p2_name, " is leading by ", (pp2-pp1), " points.")
                    print("Thanks for playing.")
                    break
            # else, the program generates a random number from 1 to 6
            # representing a dice is rolled, using randint() function
            dice = random.randint(1, 6)
            print("Dice showed: ", dice)
            # adding the dice points to the player2's score
            pp2 = pp2+dice
            # checking if there is any ladder at the player2's position
            pp2 = checkLadder(pp2)
            # checking if there is any snake at the player2's position
            pp2 = checkSnake(pp2)
            # if the player2's score is exceeding the maximum number on the board,
            # set it to maximum
            if pp2 > end:
                pp2 = end
            print(p2_name, ": Your score is ", pp2)
            if(reachedEnd(pp2)):
                print(p2_name, " won by ", (pp2-pp1), " points")
                print("Congratulations! ", p2_name)
                print("Thanks for playing.")
                break
        turn += 1


# checkLadder() function
def checkLadder(points):
    if points == 3:
        print("Hurray!! Ladder")
        return 22
    elif points == 5:
        print("Hurray!! Ladder")
        return 8
    elif points == 11:
        print("Hurray!! Ladder")
        return 26
    elif points == 20:
        print("Hurray!! Ladder")
        return 29
    else:
        return points


# checkSnake() function
def checkSnake(points):
    if points == 17:
        print("Oops!! Snake")
        return 4
    elif points == 19:
        print("Oops!! Snake")
        return 7
    elif points == 21:
        print("Oops!! Snake")
        return 9
    elif points == 27:
        print("Oops!! Snake")
        return 1
    else:
        return points

# reachedEnd method
def reachedEnd(points):
    if points == end:
        return True
    else:
        return False


# calling displayBoard() and play() functions
displayBoard()
play()