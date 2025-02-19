#2)	Faça um programa que solicite ao usuário para digitar o seu nome e um numero qualquer e em seguida exiba o seu nome varias vezes de acordo com o numero que o mesmo digitou 

Nome = input("Insira seu nome: ")
numero = int(input("Insira a quantidade de vezes que deseja repetir o seu nome: "))

for i in range(numero):
    print(Nome)

print ("Ruan Augusto Alves")