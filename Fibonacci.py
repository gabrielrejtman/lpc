# biblioteca que permite a utilização de formas através de comandos
import turtle
import math


def build_fibonacci(fibo):

    a = 0
    b = 1
    square_a = a
    square_b = b

    # definindo a cor da caneta dos quadrados
    x.pencolor("blue")

    # funções para o desenho dos quadrados
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    # variável 'temp' recebe o quadrado b, que recebe ele mesmo + o anterior
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # desenhando o resto dos quadrados
    for i in range(1, fibo):

        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)

        # temp recebe o quadrado b e quadrado b recebe ele mesmo + o anterior
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # aqui a caneta volta ao ponto que será o início da espiral (primeiro quadrado)
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # definindo a cor da caneta da espiral
    x.pencolor("red")
    x.left(90)

    for i in range(fibo):

        print(b)
        calculation = math.pi * b * factor / 2
        calculation /= 90

        for j in range(90):

            x.forward(calculation)
            x.left(1)
        temp = a
        a = b
        b = temp + b


factor = 1  # simbolizando o fator multiplicativo da função


# input para o número de elementos da sequência de Fibonacci
n = int(input("Digite a quantidade de elementos que a sequência irá rodar: "))

# definindo as condições que atendam o input
# caso o número de elementos for maior que 1, a função de criar a sequência é chamada
# caso contrário, o programa informa que o input deve ser >=1

if n > 0:
    print("Sequência de fibonacci para", n, "elementos:")
    x = turtle.Turtle()
    x.speed(100)
    build_fibonacci(n)
    turtle.done()
else:
    print("O número de elementos da sequência deve ser maior que 1")
