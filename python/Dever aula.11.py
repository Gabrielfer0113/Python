n = cont = soma = 0
while True:
   soma += n
   n = int(input('Digite um numero: [Digite 999 para interromper o progama] '))
   if n == 999:
       break
   cont += 1
print(f'A quantidade de numeros digitados foi {cont} e a soma deles é {soma}.')

# print('=--' * 25)
# print('Tabuada, para interromper o programa digite um numeor negativo.')
# print('=--' * 25)
# cont = 0
# while True:
#    t = int(input('Digite um numero: '))
#    if t < 0:
#        break
#    while cont != 10:
#        cont += 1
#        print(f'{t} X {cont} = {t * cont}')
#    cont = 0
# print('Fim do programa!!!')


# from random import randint
# esco = ''
# escopc = ''
# n = soma = 0
# vito = 0
# while True:
#    pc = randint(1, 10)
#    esco = str(input('Par ou impar: ').title())
#    if esco == 'Par':
#        escopc = 'Impar'
#        n = int(input('Escolha um numero: '))
#        soma = n + pc
#        if soma % 2 == 0:
#            print('O jogador ganhou')
#            vito += 1
#        else:
#            break
#    elif esco == 'Impar':
#        escopc = 'Par'
#        n = int(input('Digite um numero: '))
#        soma = n + pc
#        if soma % 2 == 1:
#            print('O jogador ganhou.')
#            vito += 1
#        else:
#            break
# print(f'A quantidade de vitorias do jogador foi {vito}')

# quantih = maior = idade = menorvi = 0
# while True:
#    print('=--' * 20)
#    sexo = str(input('Diga o seu sexo: [M/F] ').title())
#    if sexo != 'MF'
#       sexo = str(input('Diga o seu sexo: [M/F] ').title())
#    if sexo == 'M':
#        quantih += 1
#        idade += int(input('Diga sua idade: '))
#        if idade > 18:
#            maior += 1
#    elif sexo == 'F':
#        idade = int(input('Diga a sua idade: '))
#        if idade < 20:
#            menorvi += 1
#    sexo = str(input('Deseja continuar: [S/N] ').title())
#    if sexo == 'N':
#        break
# print(f'''A quantidade de homens são {quantih}, dentre dessa quantidade apenas {maior} homens tem acima de 18 anos
# e somente {menorvi} mulheres tem a idade menor que 20.''')


# print('=--' * 20)
# print('Loja 1.99, compre agora!!!')
# print('=--' * 20)
# tot = mil = menor = cont = 0
# barato = esco = ''
# while True:
#    produto = str(input('Digite o nome do produto: '))
#    valor = float(input('Qual é o preço do produto: '))
#    cont += 1
#    if cont == 1:
#        menor = valor
#        barato = produto
#    else:
#        if valor < menor:
#            menor = valor
#            barato = produto
#    if valor >= 1000:
#        mil += 1
#    tot += valor
#    while True:
#        esco = str(input('Deseja continuar: [S/N] ').title())
#        if esco == 'N' or 'S':
#            break
#     if esco == 'N':
#         break
# print(f'''O total gasto foi de R${tot:.2f}
# apenas {mil} produtos são um valor acima de R$1000 reais
# e o nome do produto mais barato é {barato} e custa R${menor:.2f}''')

# print('=-=' * 20)
# print('{:^60}'.format('BANCO CEV'))
# print('=-=' * 20)
# resto = cin = vin = dez = um = 0
# esco = ''
# teste = True
# while teste:
#     while True:
#         sacar = int(input('Diga o valor que deseja sacar:'))
#         cin = sacar // 50
#         resto = sacar % 50
#         if cin > 0:
#             print(f'Total de {cin} cédulas de R$50')
#         vin = resto // 20
#         resto = resto % 20
#         if vin > 0:
#             print(f'Total de {vin} cédulas de R$20')
#         dez = resto // 10
#         resto = resto % 10
#         if dez > 0:
#             print(f'Total de {dez} cédulas de R$10')
#         um = resto // 1
#         resto = resto % 1
#         if um > 0:
#             print(f'Total de {um} cédulas de R$1')
#         if resto == 0:
#             break
#     teste = False


