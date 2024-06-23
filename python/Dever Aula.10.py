# mf = str(input('Diga o seu sexo: [M/F] ').title().strip())
# while mf not in 'MF':
#     mf = str(input('Opção invalida, tente novamente: [M/F] ').title().strip())
# print(f'Sexo identificado: {mf}')

# from random import randint
# tentativa = 1
# print('=-' *25)
# pc = randint(0, 10)
# print('\033[34mVou pensar em um numero tente adivinhar...\033[m')
# jogador = int(input('Digite o seu numero: '))
# while jogador != pc:
#    tentativa += 1
#    jogador = int(input('''Você errou tente novamente.
#    '''))
# print(f'Você tentou {tentativa} vezes até acertar o numero.')

# esco = 0
# maior = 0
# num1 = int(input('Digite um numero: '))
# num2 = int(input('Digite um numero: '))
# while esco != 5:
#    esco = int(input('''Oque deseja fazer com esses numeros:
#    [1] Somar
#    [2] Multiplicar
#    [3] Qual é o maior
#    [4] Deseja escolher novos numeros
#    [5] Sair
#    Resposta: '''))
#    if esco == 1:
#        print(f'A soma de {num1} e {num2} é de {num1+num2}')
#    elif esco == 2:
#        print(f'A multiplicação de {num1} e {num2} é de {num1*num2}')
#    elif esco == 3:
#        if num1 > num2:
#            print(f'Entre esses dois numeros o maior é {num1}')
#        else:
#            print(f'Entre esses dois numeros o maior é {num2}')
#    elif esco == 4:
#        num1 = int(input('Digite um numero: '))
#        num2 = int(input('Digite um numero: '))
#    elif esco > 5:
#        print('Opção invalida tente novamente')
# print('Fim do programa, volte sempre. ☻')

# from math import factorial
# print('\033[34mDigite um numero para ver o seu fatorial\033[m')
# num = int(input('\033[34mNumero: \033[m'))
# while num != 0:
#    print(f'O fatorial de {num} é', factorial(num))
#    num = int(input('''Deseja continuar??
#    [ 0 ] Sair do programa
#    [ 1 ] Sim
#    Escolha: '''))
#    if num == 1:
#        num = int(input('\033[32mEscolha outro numero: \033[m'))
#    elif num > 1:
#        print('\033[31mOpção invalida, tente novamente.\033[m')
#        num = int(input('Escolha outro numero: '))
#    elif num == 0:
#        num = 0

# from math import factorial
# num = int(input('Digite um numero para ver o seu fatorial: '))
# sequ = num
# print(f'Calculando {num}! = ')
# while sequ > 0:
#    print(f'{sequ}', end='')
#    print(' x ' if sequ > 1 else ' = ', end='')
#    sequ -= 1
# print(f'{factorial(num)}')

# from math import factorial
# num = int(input('Diga um numero: '))
# for c in range (num, 0, -1):
#    print(f' {c} ', end='')
#    print(' x ' if c > 1 else ' = ', end='')
# print(f'{factorial(num)}', end='')

# pt = int(input('Diga o primeiro termo da progressão: '))
# razao = int(input('Diga a razão que a PA sera feita: '))
# quanti = 10
# while quanti != 0:
#    print(f' {pt}', end='')
#    print(' → ' if  quanti > 1 else '', end='')
#    pt += razao
#    quanti -= 1

# pt = int(input('Diga o primeiro termo da progressão: '))
# razao = int(input('Diga a razão que a PA sera feita: '))
# quanti = int(input('Quantas vezes a PA ira se repetir: '))
# while quanti != 0:
#    print(f' {pt}', end='')
#    print(' → ' if  quanti > 1 else '', end='')
#    pt += razao
#    quanti -= 1

# from time import sleep
# print('=--------------- Sequência de Fibonacci ---------------=')
# sequencia = int(input('''Diga um numero para começarmos a sequencia de Fibonacci.
# Numero: '''))
# primeiro = 0
# segundo = 1
# while sequencia > 0:
#    print(primeiro, end=' → ' )
#    sleep(0.5)
#    print(segundo, end='')
#    print(' → ' if sequencia > 1 else '',  end= '')
#    sleep(0.5)
#    sequencia -= 1
#    primeiro += segundo
#    segundo += primeiro

# soma = num = quanti = 0
# while num != 999:
#    num = int(input('Digite um numero, caso queira sair digite 999: '))
#    print('=--' *20)
#    soma += num
#    quanti += 1
# print(f'Você digitou {quanti - 1} numeros e sa soma deles foram {soma - 999}')

# media = 0
# soma = 0
# print('=--' *20)
# num = int(input('Digite um valor: '))
# maior = num
# menor = num
# soma += num
# num = int(input('Digite um valor: '))
# soma += num
# if maior < num:
#    maior = num
# elif menor > num:
#    menor =  num
# while num != 0:
#    print('=--' * 20)
#    num = int(input('''Deseja colocar mais numeros para a verificação da média:
# [ 0 ] NÃO
# [ 1 ] SIM
#    Resposta: '''))
#    if num == 0:
#        num = 0
#    elif num == 1:
#        print('=--' * 20)
#        num = int(input('Digite um valor: '))
#        if maior < num:
#            maior = num
#        elif menor > num:
#            menor = num
#        soma += num
#    media += 1
# print(f'A média das somas é {soma/2:.2f}, o maior numero entre eles é {maior} e o menor {menor}')
