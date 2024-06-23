# teste = list()
# teste.append('Gabriel')
# teste.append('18')
# galera = list()
# galera.append(teste[:])
# teste[0] = ('Gustavo')
# teste[1] = (40)
# galera.append(teste[:])
# print(galera) 

# galera = list()
# dados = list()
# for c in range(0, 3):
#     dados.append(str(input('Nome: ')))
#     dados.append(int(input('Idade: ')))
#     galera.append(dados[:]) # ← Caso esqueça o [:], isso dara um problema no sistema
#     dados.clear()
#     #O clear serve para limpar totalmente a lista
# print(galera)

# p = 0
# peso = list()
# pesado = list()
# leve = list()
# dados = list()
# pessoaspeso = list()
# while True:
#     pessoaspeso.append(str(input('Nome: ')))
#     pessoaspeso.append(float(input('Peso: ')))
#     if pessoaspeso[1] > 70:
#         pesado.append(pessoaspeso[0])
#     elif pessoaspeso[1] <= 70:
#         leve.append(pessoaspeso[0])
#     dados.append(pessoaspeso[:])
#     peso.append(pessoaspeso[1])
#     pessoaspeso.clear()
#     p += 1
#     esco = str(input('Deseja cadastrar mais pessoas: [Sim/Não] '))
#     if esco in 'Nn':
#         break
# print(f'''A quantidade de pessoas cadastradas foram de {p} pessoas'
#       E o maior peso foi {max(peso)} kilos e essas são as pessoas mais pesadas {pesado}
#       E o menor peso foi {min(peso)} kilos e essas pessoas são as mais leves {leve}''')

# lista = list()
# par = list()
# impar = list()
# for n in range(0, 7):
#     num = int(input(f'Digite o {n+1}° valor: '))
#     if num % 2 == 0:
#         par.append(num)
#     else:
#         impar.append(num)
# lista.append(par[:])
# lista.append(impar[:])
# print(f'Os valores pares foram \n{sorted(lista[0])} \nE os impares foram \n{sorted(lista[1])}')

# coltres = list()
# coldois = list()
# colum = list()
# num = somapar = somatres = 0
# for m in range (0, 3):
#     num = int(input(f'Digite a posição [0 , {m}]: '))
#     if m == 2:
#         somatres += num
#     colum.append(num)
#     if num % 2 == 0:
#         somapar += num
#     num = 0
# m = 0
# for m in range (0, 3):
#     num = int(input(f'Digite a posição [1 , {m}]: '))
#     if m == 2:
#         somatres += num
#     coldois.append(num)
#     if num % 2 == 0:
#         somapar += num
#     num = 0
# m = 0
# for m in range (0, 3):
#     num = int(input(f'Digite a posição [2 , {m}]: '))
#     if m == 2:
#         somatres += num
#     coltres.append(num)
#     if num % 2 == 0:
#         somapar += num
#     num = 0
# print(f'''{colum}
# {coldois}
# {coltres}''')
# print('=-' *20)
# print(f'''A soma de todos os valores pares é de {somapar}
# A soma dos valores da terceira coluna foi {somatres}
# E o maior valor da segunda linha foi {max(coldois)}''')

# from random import randint
# num = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
# jogos =  int(input('Quantos jogos deseja fazer: '))
# for c in range(jogos):
#     print(f'Jogo {c+1}: {sorted(num)}')
#     num.clear()
#     num = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]


# soma = num = n = 0
# nome = []
# nota = []
# alunos = []
# while True:
#     print('=-' * 10)
#     nome.append(str(input('Nome: ').title()))
#     for n in range(0, 2):
#         num = (float(input(f'Nota {n+1}: ')))
#         nota.append(num)
#         num = 0
#     soma = 0
#     nome.append(nota[:])
#     alunos.append(nome[:])
#     nome.clear()
#     nota.clear()
#     esco = str(input('Deseja continuar: [Sim/Não]')[0])
#     if esco in 'Nn':
#         break
# print('=-' * 20)
# print('N°', '{:<18}'.format('NOME'), 'MÉDIA')
# for aluno, contagem in enumerate(alunos):
#     print(aluno, f' {alunos[aluno][0]:<20} {sum(alunos[aluno][1])/2}')
# print('=-' * 20)
# while True:
#     escolha = int(input('Qual nota deseja ver: (999 interrompe) '))
#     if escolha == 999:
#         break
#     print(f'As notas de {alunos[escolha][0]} são {alunos[escolha][1]}')
#     print('=-' * 20)
