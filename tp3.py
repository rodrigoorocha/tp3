import psutil
import socket

info_cpu = psutil.cpu_percent(interval=1)

info_memoria = psutil.virtual_memory()

info_disco = psutil.disk_usage('.')

disco_total = round(info_disco[0] / (1024 * 1024 * 1024))

disco_uso_porcentagem = (info_disco[3])

disco_disponivel = round(info_disco[2] / (1024 * 1024 * 1024))

info_hostname = socket.gethostname()

info_rede = socket.gethostbyname(info_hostname)

opcao = 0

print("escolha a opcao ")
while opcao != 6:
    print('''
    [1]-processador    [4]-ip
    [2]-memória        [5]-Estats
    [3]-disco          [6]-Sair 

    ''')
    opcao = int(input('escolha a opçao '))
    if opcao == 1:
        print(f'\nUso da Cpu = ', info_cpu, '%')

    if opcao == 2:
        print('\nPorcentagem do uso de memória =', info_memoria[2], '%')

    if opcao == 3:
        print(f'\nTamanho do disco = ', disco_total, 'GB '
                                                     ' Utilizado = ', disco_uso_porcentagem, '% '
                                                                                             ' Disponivel =',
              disco_disponivel, 'GB')

    if opcao == 4:
        print('\nEndereço IP =', info_rede)

    if opcao == 5:
        print('\nEstats=\nUso da CPU=', info_cpu, '%'
                                                  '\nuso da Memória=', info_memoria[2], '%'
                                                                                        '\nespaço em disco disponível= ',
              disco_disponivel, 'GB'
                                '\nendereço ip=', info_rede

              )

    if opcao == 6:
        print('\nsaindo')

    else:
        print('coloque um numero valido')
    print('**********************************')
    print('**********************************')

