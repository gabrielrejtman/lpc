# Objetivo do Jogo: O primeiro jogador que levar a tartaruga a sua casa vence
# Como jogar: Jogo de turnos; cada jogador rola um dado e o resultado * 20
# o número de casas que andará com sua tartaruga

import random
import turtle

# abaixo, definição de cor, ícone e posição inicial dos jogadores

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

# abaixo, os pontos de chegada das tartarugas, representados por círculos de cores correspondentes

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

# abaixo, criação de um 'dado' utilizando lista
dice = [1, 2, 3, 4, 5, 6]

# checando se algum jogador atingiu seu objetivo (equivalente a vitória)

for i in range(20):

    if player_one.pos() >= (300, 100):

        print("Vitória do jogador 1!")
        break
    elif player_two.pos() >= (300, -100):
        print("Vitória do jogador 2!")
        break
# caso não seja o caso, ocorre a rolagem dos dados automaticamente ao apertar 'enter'
    else:
        # vez do jogador 1
        player_one_turn = input("Pressione 'Enter' para rolar os dados ")
        dice_outcome = random.choice(dice)  # escolhe um numero automaticamente da lista do dado
        print("O resultado do dado é: ")
        print(dice_outcome)
        print("O número de passos será: ")
        print(20 * dice_outcome)
        player_one.fd(20 * dice_outcome)  # número de passos andados é equivalente a 20x o resultado do dado
        # vez do jogador 2
        player_two_turn = input("Pressione 'Enter' para rolar os dados ")
        dice_outcome = random.choice(dice)  # escolhe um numero automaticamente da lista do dado
        print("O resultado do dado é: ")
        print(dice_outcome)
        print("O número de passos será: ")
        print(20 * dice_outcome)
        player_two.fd(20 * dice_outcome)
