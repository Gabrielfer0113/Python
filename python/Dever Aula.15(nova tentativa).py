# def area(l, c):
#     a = l * c
#     print(f'A area do terreno é: {a:.2f}')


# lar = float(input('Largura: '))
# comp = float(input('Comprimento: '))
# area(lar, comp)

# def escreva(p):
#     tam = len(p) + 4
#     print('-' * tam)
#     print(f'  {p}')
#     print('-' * tam)

# pal = str(input('Digite alguma coisa: '))
# escreva(pal)

# linha = '-=' * 20
# from time import sleep
# def contador(i, f, p):
#     if p == 0:
#         p = 1
#     elif p < 0:
#         p = 1
#     print(f'Contador de {i} até {f} pulando de {p} um em {p}')
#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f'{cont}', end=' ', flush=True)
#             sleep(0.2)
#             cont += p
#         print('Fim\n',linha)
#     else:
#         cont = i
#         while cont >= f:
#             print(f'{cont}', end=' ', flush=True)
#             cont -= p
#             sleep(0.2)
#         print('Fim\n', linha)


# contador(1, 10, 1)
# contador(10, 0, 1)
# print('Agora é sua vez:')
# i = int(input('Inicio: '))
# fim = int(input('Final: '))
# passo = int(input('Passo: '))
# contador(i, fim, passo)

# from time import sleep
# from random import randint 
# linha = '-=' * 20
# def maior(*n):
#     print(linha)    
#     print('Analizando os valores passados...')
#     for i in n:
#         print(f'{i} ', end='', flush=True)
#         sleep(0.3)
#     print(f'Foram informados {len(n)} valores ao todo')
#     print(f'O maior valor informado foi {max(n)}', flush=True)
#     sleep(3)


# maior(randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
# maior(randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
# maior(randint(1, 9), randint(1, 9), randint(1, 9))
# maior(randint(1, 9), randint(1, 9))
# maior(randint(1, 9))

from time import sleep
from random import randint
def sorteia(lista):
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)


def pares(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nA soma dos valores pares são {soma}')

numeros = list()
sorteia(numeros)
pares(numeros)

