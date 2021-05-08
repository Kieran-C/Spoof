import random


def swapPlayer(playerNum):
    if playerNum == 1:
        return 2
    else:
        return 1


def game():
    randomNum = random.randrange(15, 20)
    print("The number of coins on the table: ", randomNum)
    gamePlay = True
    playerToken = 1

    while gamePlay:
        if playerToken == 1:
            userInput = input("\nEnter the amount of coins to take: ")
        else:
            userInput = random.randrange(1, 4)
        if (randomNum - int(userInput)) <= 0:
            print("Player %s won!" % swapPlayer(playerToken))
            break
        else:
            randomNum -= int(userInput)
        print("Coins you took: ", userInput)
        print("The number of coins on the table: ", randomNum)
        playerToken = swapPlayer(playerToken)


game()
