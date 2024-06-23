# valor = list()
# for v in range(0,5):
#     valor.append(int(input(f'Diga um valor da posição {v}: ')))  
#     if v == 4:
#         break
# print(f'O maior valor é {max(valor):.0f} e sua posição é ', end='') 
# for i, v in enumerate(valor):
#     if v == max(valor):
#         print(f'{i}', end=' ')
# print(f'\nO menor valor é {min(valor):.0f} e sua posição é ', end='')
# for i, v in enumerate(valor):       
#     if v == min(valor):
#         print(f'{i}', end=' ')

# lista = list()
# while True:
#     num = int(input('Digite um valor: '))
#     if num not in lista:
#         lista.append(num)
#     else:
#         print('Valor repetido, não irei memorizalo')
#     esco = str(input('Deseja continuar: [Sim/Não] ')[0])
#     if esco in 'Nn':
#         break
# print(f'A ordem crescente dos resultados foi {sorted(lista)}')

# quanti = 0
# lista = list()
# while True:
#     lista.append(int(input('Digite um numero: ')))
#     esco = str(input('Deseja continuar: [Sim/Não] '))
#     lista.sort(reverse=True)
#     if esco in 'Nn':
#         break
# print(f'''A quantidade de numeros digitados foram de {len(lista)}
# o valor na ordem decrescente é {lista}''')
# if 5 in lista:
#     print('O valor 5 esta na lista')
# else:
#     print('O valor 5 não esta na lista')


# lista = list()
# par = list()
# impar = list()
# while True:
#     num = int(input('Digite um numero: '))
#     if num % 2 == 0:
#         par.append(num)
#     else:
#         impar.append(num)
#     lista.append(num)
#     esco = str(input('Deseja continuar: [Sim/Não] '))
#     if esco in 'Nn':
#         break
# print(f'''A lista completa é {lista}
# Os numeros pares {par}
# Os numeros impares {impar}''')

# expressão = str(input('Digite uma expressão matematica: '))
# paren = []
# for item in expressão:
#     if item == '(':
#         paren.append('(')
#     elif item == ')':
#         if len(paren) > 0:
#             paren.pop()
#         else:
#             paren.append(')')
#             break
# if len(paren) == 0:
#     print('A expressão esta correta!!')
# else:
#     print('A expressão esta incorreta!!!')

#REFAZENDO EXERCICIOS QUE EU FIQUE COM UM POUCO EM DUVIDA

# lista = []
# for n in range(0, 5):
#     lista.append(int(input('Digite um valor: ')))
# for i, n in enumerate(lista):
#     if n == max(lista):
#         print(f'\nO maior valor foi {max(lista)} e esta na {i + 1}° posição')
# for i, n in enumerate(lista):
#     if n ==  min(lista):
#         print(f'E o menor valor é {min(lista)} e esta na {i + 1}° posição')

# numeros = []
# while True:
#     num = int(input('Digite um valor: '))
#     if num not in numeros:
#         numeros.append(num)
#     else:
#         print('Valor repetido, não irei adiciona-lo')
#     esco = str(input('Deseja continuar? [Sim/Não] '))
#     if esco in 'Nn':
#         break
# print(f'Os a lista foi {numeros} e eles em ordem crescente foi {sorted(numeros)}')
# n = 0
# num = []
# while True:
#     num.append(int(input('Digite um numero: ')))
#     n += 1
#     esco = str(input('Deseja continuar: [Sim/Não] '))
#     if esco in 'Nn':
#         break
# num.sort(reverse=True)
# print(f'foram digitados {n} numeros, a ordem decrescente dos numeros é {num}')
# if 5 in num:
#     print('O valor 5 esta na lista')
# else:
#     print('O valor 5 não foi colocado na lista')

# lista = []
# par = []
# impar = []
# while True:
#     num = int(input('Escreva um numero: '))
#     if num % 2 == 0:
#         par.append(num)
#     else:
#         impar.append(num)
#     lista.append(num)
#     esco = str(input('Deseja continuar: [Sim/Não] '))
#     if esco in 'Nn':
#         break
# print(f'''A lista inteira foi {lista}
# Os numeros pares foram {par}
# Os numeros impares foram {impar}''')
