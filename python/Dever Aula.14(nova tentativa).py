# aluno = dict()
# aluno['Nome'] = str(input('Nome do aluno:')).title()
# aluno['Nota'] = float(input('Nota: '))
# if (aluno['Nota'] < 5):
#     print(f'O aluno {aluno["Nome"]} tirou {aluno["Nota"]} logo a situação é reprovado/a')
# elif (aluno['Nota'] < 7):
#     print(f'O aluno {aluno["Nome"]} tirou {aluno["Nota"]} logo ele esta de recuperação.')
# else:
#     print(f'O aluno {aluno["Nome"]} tirou {aluno["Nota"]} logo ele esta aprovado') 

# from random import randint
# from operator import itemgetter
# from time import sleep
# rank = list()
# jogo = dict()
# jogo = {'jogador01': randint(1,6),
#         'jogador02': randint(1,6),
#         'jogador03': randint(1,6),
#         'jogador04': randint(1,6)}
# for k,v in jogo.items():
#     print(f'O {k} tirou {v}')
#     sleep(0.7)
# print('Ranking dos jogadores:')
# rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# for i, v in enumerate(rank):
#     print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
#     sleep(0.7)


# from datetime import datetime
# linha = str('------------------------------ = ------------------------------')
# pessoa = dict()
# pessoa['Nome'] = str(input('Nome: ')).title()
# pessoa['Ano de nascimento'] = int(input('Ano de nascimento: '))
# pessoa['carteira de trabalho'] = int(input('CTPS: [0 caso não tenha]'))
# if (pessoa['carteira de trabalho'] <= 0):
#     print(linha)
# else:
#     pessoa['ano contratação'] = int(input('Ano de contratação: '))
#     pessoa['salario'] = float(input('Salario: '))
#     print(linha)
# for k, v in pessoa.items():
#     print(f'{k} tem valor {v}')
# if (pessoa['carteira de trabalho'] <= 0):
#     print('')
# else:
#     print(f'A sua idade atual é de {datetime.now().year - pessoa["Ano de nascimento"]}')
#     print(f'E você ira se aposentar com {35 - (datetime.now().year - pessoa["ano contratação"] ) + (datetime.now().year - pessoa["Ano de nascimento"])} anos')
#     print(linha)

# linha = str('--------------------------- = ---------------------------')
# gols = list()
# jogador = dict()
# jogador['Nome'] = str(input('Nome do jogador: ')).title()
# jogos = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
# print (linha)
# for j in range(jogos):
#     gols.append(int(input(f'Quantos gols ele fez no {j+1}° jogo: ')))
#     jogador ['gols'] = gols[:]
# jogador ['total'] = sum(jogador['gols'])
# print(linha)
# for k, v in jogador.items():
#     print(f'O campo {k} tem valor {v}')
# print(linha)
# print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas:')
# for j, v in enumerate(jogador['gols']):                                             #####QUANDO TIVER LISTA DENTRO DE DICIONARIO LEMBRE DE CONSIDERAR O 'ENUMERATE'
#     print(f' →Na partida {j+1}, fez {v} gols.')

# linha = str('------------------------------- = -------------------------------')
# pessoas = list()
# acima_media = list()
# dados = dict()
# media_idade = 0
# while True:
#     dados.clear()
#     dados['nome'] = str(input('Nome: ')).title()
#     while True:
#         dados['sexo'] = str(input('Sexo: [M/F] ')).title()
#         if dados['sexo'] in 'MF':
#             break
#         print('Os valores aceitos são somente M e F!!!')
#     dados['idade'] = int(input('Idade: '))
#     media_idade += dados['idade']
#     pessoas.append(dados.copy())
#     while True:
#         esco = str(input('Deseja continuar: [S/N] ')).title()
#         if esco in 'SN':
#             break   
#         print('Os valores aceitos são somente S ou N!!!')
#     if esco in 'N':
#         break
#     print(linha)
# print(f'A quantidade de pessoas cadastradas foram de {len(pessoas)} pessoas.')
# print(f'A média de idade é {media_idade / len(pessoas):5.2f} anos')
# print(f'As mulheres cadastradas foram: ', end=' ')
# for m in pessoas:
#     if m['sexo'] in 'Ff':
#         print(f'{m["nome"]}', end=' ')
# for p in pessoas:
#     if p['idade'] > media_idade / len(pessoas):
#         print(f'\nAs pessoas acima da media das idades cadastradas foram {p["nome"]}')

linha = str('--------------------------- = ---------------------------')
gols = list()
jogador = dict()
jogadores = list()
while True:
    gols.clear()
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: ')).title()
    jogos = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    print(linha)
    for j in range(jogos):
        gols.append(int(input(f'Quantos gols ele fez no {j+1}° jogo: ')))
        jogador ['gols'] = gols[:]
    jogador ['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    esco = input(str('Deseja colocar mais jogadores: [S/N] ')).title()
    if esco in 'Nn':
        break
print(linha)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<16}', end='')
    print()
print(linha)
while True:
    busca = int(input('Mostrar dados de qual jogador: [999 para parar]'))
    print()
    if busca == 999:
        break
    if busca >= len(jogador):
        print(f'ERRO! Não exite jogador com código {busca}')
        print(linha)
    else:
        print(f'----- LEVANTAMENTO DO JOGADOR {jogadores[busca]["Nome"]}')
        for j, g in enumerate(jogadores[busca]["gols"]):
            print(f'Na partida {j+1} ele fez {g} gols.')
        print(linha)