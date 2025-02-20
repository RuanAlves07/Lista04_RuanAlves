#EXE 012 - Você é um desenvolvedor de sistemas trabalhando em um projeto para um salão de beleza. O salão precisa de um sistema para gerenciar os horários de atendimento dos clientes. Primeiro, a dona do salão monta a grade horária da agenda. Depois, uma cliente deseja agendar um horário, e o sistema exibe os horários disponíveis. A dona do salão então agenda o horário escolhido pela cliente, e o horário escolhido não estará mais disponível. O sistema deve continuar permitindo agendamentos até que todos os horários disponíveis sejam preenchidos ou até que a dona do salão decida parar.
#Desenvolva um programa em Python que:
#1.	Solicite à dona do salão para inserir os horários disponíveis na agenda.
#2.	Exiba os horários disponíveis para a cliente.
#3.	Permita que a cliente escolha um horário para agendamento.
#4.	Atualize a agenda marcando o horário escolhido como ocupado.
#5.	Pergunte se deseja agendar mais um horário e continue até que todos os horários estejam preenchidos ou a dona do salão decida parar.


horarios = []

qntd_horas = int(input("Insira quantas horas estão disponiveis: "))

for i in range(qntd_horas):
    horas_disponiveis = str(input("Digite o horário disponivel: "))
    horarios.append(horas_disponiveis)

for i in range(len(horas_disponiveis)):
    print("Horarios disponiveis: \n{}".format(horarios))
    for i, horas_disponiveis in enumerate(horarios):
        print("{} - {}".format(i+1, horas_disponiveis))
    escolher_horario = int(input("Escolha um dos hórarios disponiveis: "))

    if 1 <= escolher_horario <= len(horas_disponiveis):
        horario_selecionado = horas_disponiveis[escolher_horario - 1]
        print("O horário {} foi agendado com sucesso!".format(horas_disponiveis))
        

    if len(horario_selecionado) == 0:
        print("Todos os horarios estão ocupados!")
        break
    continuar = input("Deseja adicionar mais um horário? (S/N): ")

    if continuar == "n" or "N":
        print("Programa encerrando...")
        break
    

#meudeus que bagulho embaçado   

