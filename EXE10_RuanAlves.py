#Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
#	Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa". 
#	Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".

convite = int(input("Insira quantas pessoas você deseja convidar: "))

convites = []

if convite < 10:
    for i in range(convite):
        nomes_convites = input("Informe o nome das pessoas convidadas: ")
        convites.append(nomes_convites)
        print("{} está convidado(a) para a festa.".format(convites))
else:
    print("Numero muito alto!")


