#7)	Peça ao usuário para inserir seu nome e um numero. Se o numero for menor que 10 (<), exiba o nome dele esse numero de vezes, caso contrario exiba a mensagem “Numero muito alto!” 3x

nome = input("Insira seu nome: ")
numero = int(input("Insira seu numero: "))

if numero < 10:
    for i in range(numero):
        print(nome)
else: 
    for i in range(3):
        print("Numero muito alto!")

print ("Ruan Augusto Alves")