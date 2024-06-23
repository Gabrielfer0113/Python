# num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'novo', 'dez',
# 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'vinte')
# while True:
#     esco = int(input('Digite um numero de 0 até 20: '))
#     if 0 <= esco <= 20:
#         break
#     print('Tente novamente. ', end='')
# print('O numero por extenso é', num[esco])

# times = ('Palmeiras', 'Gremio', 'Atletico-MG', 'Flamengo', 'Bota fogo', 'Red Bull Bragantino', 'Fluminense', 'Athletico-r', 'Internacional',
# 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
# print('=--' * 30)
# print('{:^90}'.format('BRAZILEIRÃO'))
# print('=--' * 30)
# print('Os cinco primeros times do brasileirão são:\n', times[0:5])
# print('=--' * 30)
# print('Os ultimos quatro times são:\n', times[16:20])
# print('=--' * 30)
# print('A ordem alfebética desses times é:\n', sorted(times))
# print('=--' * 30)
# print('E o time Vasco esta na', times.index('Vasco')+1,'posição ')

# from random import randint
# aleatório = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
# print('A sequencia de numeros foi: ', aleatório)
# print('O menor numero entre os resultados foi:', max(aleatório))
# print('E o menor foi:', min(aleatório))
# O 'max' e 'min' são funcionais em Tuplas, são uteis em alguns casos

# numeros = (int(input('Digite um numero entre 0 e 9: ')),
#             int(input('Digite um numero entre 0 e 9: ')),
#             int(input('Digite um numero entre 0 e 9: ')),
#             int(input('Digite um numero entre 0 e 9: ')))
# soma = 0
# print('=--' * 20)
# if not 9 in numeros:
#     print('O numero 9 não apareceu nas escolhas acima.')
# elif 9 in numeros:
#     if numeros.count(9) > 1:
#         print(f'O numero 9 apareceu {numeros.count(9)} vezes.')
#     elif numeros.count(9) == 1:
#         print(f'O numero 9 apareceu {numeros.count(9)} vez.')
# print('=--' * 20)
# if 3 in numeros:
#     print(f'O numero 3 apareceu pela primeira vez na localização {numeros.index(3)+1}')
# else:
#     print('O numero 3 não foi encontrado nas posições acima.')
# print('=--' * 20)
# print('Os valores pares digitados são: ', end='')
# for n in numeros:
#     if n % 2 == 0:
#        print(n, end=' ')

print('=--' * 20)
print('{:^60}'.format('Lista de preços'))
print('=--' * 20)
itens = ('lapis', 1.75,
        'Borracha', 2.00,
        'Caderno', 15.90,
        'Estojo', 25.00,
        'Transferidor', 4.20,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'Livro', 34.90)
print('=--' * 20)
for n in range(0, len(itens)):
    if n % 2 == 0:
        print(f'{itens[n]:.<30} R$', end='')
    else:
        print(f'{itens[n]:>7.2f}')

# ESSE EXERCICIO ABAIXO FOI FEITO A MAIS POR CONTA DE EU N TER PEGADO O MACETE

# compras = ('arroz', 15.00,
#             'feijão', 6.70,
#             'File de frango', 12.55,
#             'Alface', 3.99)
# print('{:-^40}'.format('Compras'))
# for itens in range (0, len(compras)):
#     if itens % 2 == 0:
#         print(f'{compras[itens]:.<30} R$', end='')
#     else:
#         print(f'{compras[itens]:6.2f}')

# print('=--' * 10)
# palavras = ('Teclado',
#             'Televisao',
#             'Mouse',
#             'Computador')
# for vogal in palavras:
#     print(f'\nNa palavra {vogal} temos ', end='')
#     for letra in vogal:
#         if letra.lower() in 'aeiou':
#             print(letra, end=' ')

# ESSE EXERCICIO ABAIXO FOI FEITO A MAIS POR CONTA DE EU N TER PEGADO O MACETE

# amor = ('Paixao',
#         'Amor',
#         'Confiança',
#         'Tesao',
#         'Odio' )
# for sentimentos in amor:
#     print(f'\nOs setimentos {sentimentos} tem as vogais ', end='')
#     for duvida in sentimentos:
#         if duvida.lower() in 'aeiou':
#             print(f'{duvida}', end=' ')


# flores = ('tulipa', 12.99,
#         'Dama-da-noite', 19.50,
#         'rosa', 14.00,
#         'orquidea', 20.00)
# for flor in range(len(flores)):
#     if flor % 2 == 0:
#         print(f'{flores[flor]:.<20} R$', end=' ')
#     else:
#         print(f'{flores[flor]}')

# palavras = ('Rosa', 
#             'Dama-da-noite', 
#             'Orquidea', 
#             'Tulipa')
# for flor in palavras:
#     print(f'\nNas palavras {flor.upper()} tem as vogais ', end='')
#     for flores in flor:
#         if flores.lower() in 'aeiou':
#             print(flores, end=' ')