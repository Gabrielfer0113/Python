# aluno = {'Nome': str(input('Nome: ').title())}
# aluno['Nota'] = float(input(f'Qual é a média de {aluno["Nome"]}: '))
# if aluno["Nota"] > 6:
#     print(f'A situação de {aluno["Nome"]} é aprovado')
# elif 5 <= aluno["Nota"] < 6:
#     print(f'A situação de {aluno["Nome"]} é recuperação')
# elif aluno["Nota"] < 5:
#     print(f'A situação de {aluno["Nome"]} é reprovado')

# from random import randint
# from time import sleep
# jogadores = {"Jogador01": randint(1 , 6),
#              "Jogador02": randint(1 , 6),
#              "Jogador03": randint(1 , 6),
#              "Jogador04": randint(1 , 6)}
# print ('Valores sorteados: ')
# for i in sorted(jogadores, key = jogadores.get, reverse=True):
#     print(i,f'tirou {jogadores[i]} no dado')
#     sleep(0.7)

# from datetime import datetime
# contratado = {}
# contratado ['Nome'] = str(input('Nome: ').title())
# contratado ['nascimento'] = int(input('Data de nascimento: '))
# contratado ['idade'] = datetime.now().year - contratado['nascimento'] 
# contratado ['CTPS'] = int(input('Carteira de trabalho: (digite 0 caso não tenha) '))
# if contratado['CTPS'] != 0:
#     contratado ['ano de contratação'] = int(input('Qual é o seu ano de contratação: '))
#     contratado ['salario'] = float(input('Salario: '))
#     contratado ['aposentadoria'] = (35 -(datetime.now().year - contratado['ano de contratação'])) + contratado['idade']
# print('=-' * 30)
# for i, c in contratado.items():
#     print(f'{cores["verde"]}{i}{cores["limpo"]} tem o valor de {cores["azul"]}{c}{cores["limpo"]}')
#     print('')

# gols = []
# jogador = {'nome': str(input('Nome do jogador: ').title())}
# partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
# for i in range(partidas):
#     gols.append (int(input(f'Quantos gols ele fez no {i+1}° jogo: ')))
# print('=-' * 30)
# jogador ["gols"] = gols
# jogador ["total"] = sum(gols)
# for j, g in jogador.items():
#     print (f'O campo {j} tem valor de {g}')
# print('=-' * 30)
# print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
# for p, g in enumerate(jogador['gols']):
#     print(f'-> No {p+1}° jogo ele fez {g} ')

#ATIVIDADE DE EXEMPLO, ESTUDO ↓↓↓
# galera = list()
# pessoa = dict()
# soma = media = 0
# while True:
#     pessoa.clear()
#     pessoa['nome'] = str(input('Nome: ')).title()
#     while True:
#         pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
#         if pessoa['sexo'] in 'MF':
#             break
#         print('ERRO! por favor, digite apenas M ou F.')
#     pessoa['idade'] = int(input('Idade: '))
#     soma += pessoa['idade']
#     galera.append(pessoa.copy())
#     while True:
#         resp = str(input('Quer continuar?? [S/N] ')).upper()[0]
#         if resp in 'SN':
#             break
#         print('ERRO! Responda com apenas S ou N.')
#     if resp == 'N':
#         break
# media = soma / len(pessoa)
# print('-=' * 30)
# print(f'A) A quantidade de pessoas cadastradas foram de {len(galera)}  pessoas')
# print(f'B) A média de idade das pessoas foram de {media:5.2f} ')
# print('C) As mulheres cadastradas foram ', end='')
# for p in galera:
#     if p['sexo'] in 'Ff':
#         print(f'{p["nome"]} ', end='')
# print()
# print('D) Lista das pessoas que estão acima da média: ')
# for p in galera:
#     if p['idade'] >= media:
#         print('    ')
#         for k, v in p.items():
#             print(f'{k} = {v} ', end='')
#         print()
# print('<< ENCERRADO >>')
#ATIVIDADE DE EXEMPLO, ESTUDO ↑↑↑

grupo = list()
pessoa = dict()
soma = media_idade = 0
while True:
    pessoa.clear()
    print('---------------- = ----------------')
    pessoa['nome'] = str(input('NOME: ')).title()
    while True:
        pessoa['sexo'] = str(input('SEXO: [M/F] ')).title()
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Tente responder somente com M ou F.')
    pessoa['idade'] = int(input('IDADE: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        esco = str(input('Deseja continuar: [S/N] ')).title()
        if esco in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if esco == 'N':
        break
media_idade = soma / len(grupo)
print('---------------- = ----------------')
print(f'A)A quantidade de pessoas cadastradas foram {len(grupo)} pessoas')
print(f'B)A média das idades é {media_idade:5.2f}')
print('C)As mulheres cadastradas foram', end=' ')
for p in grupo:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print('\nD)As pessoas com a idade acima da média foram', end=' ')
for p in grupo:
    if p['idade'] >= media_idade:
        print(f'{p["nome"]}', end=' ')
print('\n<< Programa encerrado >>')

