#Rock Paper Scissor in Python

import random
import time
rock = 1
paper = 2
scissor = 3
names = {rock : "Rock", paper : "Paper", scissor : "Scissor"}
#Rules that Define the Player's Winning Scenario
condition = {rock : scissor, paper : rock, scissor : rock}
#Initializes player's score and computer's score to 0
computer_score = 0
player_score = 0
# start the game
def start():
    print("Let's start with the Game of Rock, Paper and Scissor")
    while game():
        pass
    scores()

def game():
    """This method calls for player's move and passes the player's choice to result function to compare both"""
    player = move()
    #Makes a random move for computer out [1, 2, 3]
    computer = random.randint(1, 3)
    #check for result player and computers move
    result(player, computer)
    return (play_again())

def move():
    """This function handles player choice of either Rock, Paper or Scissor"""
    while True:
        print()
        player  = input("Rock = 1\n Paper = 2\nScissor = 3\nMake A Move : ")
        try :
            #check if player entered a valid input
            player = int(player)
            if player in [1,2,3]:
                return player
            #if invalid input raise Error
        except ValueError:
            pass
        print("Oops! I didn't understand that. please enter 1, 2 or 3.")


def result(player, computer):
    """Evaluates result out of Player's Choice and Computer's Choice"""
    for i in range(1, 4):
        print("." * i, )
        # makes execution stop for 1 sec
        time.sleep(1)
        print("", end="")
    # print Computer's random choice out of [1, 2, 3]
    print("Computer throw {0}!".format(names[computer]))
    global player_score, computer_score
    # if choice of Player and Computer are equal print Tie Game
    if player == computer:
        print("Tie Game")
    else:
        # check if Player's Choice an Computer's Choice make a win for Player
        if condition[player] == computer:
            print("Aha !, You have won")
            player_score += 1
        # if not return Player lost
        else:
            print("You are no better than ME . You Lost")
            computer_score += 1


def play_again():
    """Prompts User To Play again"""
    scores()
    answer = input("Would You Like To play Again (y/n):")
    if answer in ["y", "Y"]:
        return answer
    else:
        # if player says no then greet him and exit()
        print("Thank You very much for playing our Game .See you next Time!.")

def scores():
    """prints Scores of both computer and player"""
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player :",player_score)
    print("Computer : ",computer_score)
if __name__ == "__main__":
    start()
