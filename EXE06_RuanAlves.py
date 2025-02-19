#6)	Peça um numero abaixo de 50 e em seguida faça um contagem regressiva de 50 até esse número, certificando-se de mostrar o numero que eles inseriram na saída

numero = int(input("Insira um numero: "))

for i in range(numero):
    numero1 = numero - i
    print(numero1)
    
    if numero == i:
        break

print ("Ruan Augusto Alves")