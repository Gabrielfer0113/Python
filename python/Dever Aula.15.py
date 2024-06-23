# def area(larg, comp):
#     a = larg * comp
#     print(f'A area de um terreno {larg}X{comp} é de {a}m²')


# print('Controle de Terrenos')
# print('-' * 20)
# l = float(input('Largura (m): '))
# c = float(input('Comprimento (m): '))
# area(l, c)

# def linha(l):
#     dis = len(l) + 4
#     print(f'-' * dis)
#     print(f'  {palavra}')
#     print(f'-' * dis)


# palavra = str(input('Digite alguma palavra: '))
# linha(palavra)

# from time import sleep
# linha = str('----------------------------------------')
# def contador(i, f, p):
#     # if p < 0:
#     #     p = -(p)
#     # if p == 0:
#     #     p = 1
#     # print(linha)
#     # print(f'Contagem de {i} até {f} de {p} em {p}')

#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f'{cont} ', end='', flush=True)
#             sleep(0.2)
#             cont += p
#         print('Fim\n', linha)
#     else:
#         cont = i
#         while cont >= f:
#             print(f'{cont} ', end='', flush=True)
#             sleep(0.2)
#             cont -= p
#         print('Fim\n', linha)


# contador(1, 10, 1)
# contador(10, 0, 1)
# print('Agora é sua vez: ')
# inicio = int(input('Inicio: '))
# fim = int(input('Final: '))
# passo = int(input('Passo: '))
# contador(inicio, fim, passo)

# from time import sleep
# from random import randint
# def numeros(*num):
#     print('-=' * 20)
#     print('Analizando os valores passados...')
#     for valor in num:
#         print(f'{valor} ', end='', flush=True)
#         sleep(0.5)
#     print(f'foram informados {len(num)} valores ao todo.')
#     print(f'E o maior deles foi: {max(num)}', flush=True)
#     sleep(2)


# numeros(randint(0, 9),randint(0, 9),randint(0, 9),randint(0, 9),randint(0, 9))
# numeros(randint(0, 9),randint(0, 9),randint(0, 9))
# numeros(randint(0, 9),randint(0, 9))
# numeros(randint(0, 9))
# print('-=' * 20)


# from time import sleep
# from random import randint
# def sorteia(lista):  
#     print('Sorteando 5 valores da lista: ', end='')
#     for cont in range(0, 5):
#         n = randint(1, 10)
#         lista.append(n)
#         print(f'{n} ', end='', flush=True)
#         sleep(0.5)
#     print('PRONTO!!')

# def somaPar(lista):
#     soma = 0
#     for valor in lista:
#         if valor % 2 == 0:
#             soma += valor
#     print(f'A soma dos valores pares foram de {soma}')



# numeros = list()
# sorteia(numeros)
# somaPar(numeros)


