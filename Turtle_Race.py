# Main goal: The first player to reach his turtle's house wins.
# How to play: Each player has a turn. In every turn, the player 
# must roll a die and walk 20 times the result that he's gotten.

import random
import turtle

# down below, players initial positions, icons and color definitions

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

# down below, the turtles objectives, represented by matching-color circles

player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

# creating a die using a list
dice = [1, 2, 3, 4, 5, 6]

# checking if some player has reached the objective

for i in range(20):

    if player_one.pos() >= (300, 100):

        print("Player 1 Won!")
        break
    elif player_two.pos() >= (300, -100):
        print("Player 2 Won!")
        break
# in case that does not occur, a player must press 'enter' to roll a die
    else:
        # player 1 turn
        player_one_turn = input("Press 'Enter' to roll a die")
        dice_outcome = random.choice(dice)  # chooses a random number from the dice
        print("The outcome is: ")
        print(dice_outcome)
        print("The number of steps is: ")
        print(20 * dice_outcome)
        player_one.fd(20 * dice_outcome)  # the number of steps taken is equivalent to the die result * 20
        # player 2 turn
        player_two_turn = input("Press 'Enter' to roll a die")
        dice_outcome = random.choice(dice)  # chooses a random number from the dice
        print("The outcome is: ")
        print(dice_outcome)
        print("The number of steps is: ")
        print(20 * dice_outcome)
        player_two.fd(20 * dice_outcome)
