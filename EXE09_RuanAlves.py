#Faça um programa que pergunte em qual direção o usuário deseja contar (para cima [ c/C] ou para baixo [a/A]).
#	Se ele selecionar para cima, peça o número superior e conte de 1 até esse número.
#	Se ele selecionar para baixo, peça-lhe para inserir um número abaixo de 20 e, em seguida, faça uma contagem regressiva de 20 até esse número.
#	Se ele inserir algo diferente de cima ou baixo, exiba a mensagem “Direção Invalida!".


direção = input("Diga a direção que deseja apontar: (C para cima, A para baixo)")

if direção == "A":
    numero = int(input("qual o numero que deseja? (Abaixo de 20)"))
    for i in range(20,numero -1 ,-1):
        print(i)
elif direção == "C":
    numero = int(input("qual o numero que deseja? (Superior a 1)"))
    for i in range(numero + 1):
        print(i)

print ("Ruan Augusto Alves")