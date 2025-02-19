#8)	Defina uma variável chamada total como zero (0). Peça ao usuário para inserir cinco números e, após cada entrada pergunte se ele deseja que esse numero seja incluído (S ou s, N ou n). Se ele desejar, adicione o numero ao total. Se ele não quiser inclui-lo, não adicione ao total. Depois de inserir todos os cinco números, exiba o total.

total = 0

for i in range(5):
    numero = int(input("Insira cinco numeros: "))
    pergunta = input("Deseja continuar?")

    if pergunta == "s":
        total += numero

print("Total deu: {}".format(total))