#5)	Peça ao usuário para inserir um número que deseja da tabuada e em seguida exibir a tabuada desse número.

numero = int(input("Insira um numero para a tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print("{} x {} = {}".format(numero, i, resultado))

print ("Ruan Augusto Alves")