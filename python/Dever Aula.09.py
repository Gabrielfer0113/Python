# from time import sleep
# for fogos in range(10, 0, -1):
#    print(fogos)
#    sleep(1)
# print('A queima de fogos começou, \033[32mfeliz ano novo!!!\033[m')

# for pares in range(0, 51, 2):
#    print(pares, end=' ')

# b = 0
# for tmulti in range (1, 501, 2):
#     if tmulti % 3 == 0:
#         b += tmulti
# print(f'A soma dos numeros impares até 500 é de {b}')

# a = int(input('Digite o numero a ser multiplicado: '))
# b =  int(input('Digite a quantidade de vezes que esse numero sera multiplicado: '))
# for tabuada in range (0 + 1, b + 1):
#    print(a, 'X', tabuada, '=',  a * tabuada)

# b = 0
# for imparpar in range (0, 6):
#    a = int(input('Digite um numero inteiro: '))
#    if a % 2 == 0:
#        b += a
# print(f'O valor da soma dos numeros pares é de: {b}')

# termo = int(input('Digite o primeiro termo da progressão aritmética: '))
# razao = int(input('Digite a razão dessse termo: '))
# vezes = int(input('Diga a quantidade de vezes que deseja repetir: '))
# for pa in range (0, vezes):
#    print(termo, end=' \033[33m|\033[m ')
#    termo += razao

# tot = 0
# n = int(input('Escreva um numero: '))
# for c in range (1, n + 1):
#    if n % c == 0:
#        print('\033[32m', end='')
#        tot += 1
#    else:
#        print('\033[31m', end='')
#    print(c, end=' → ')
# print('Fim\033[m')
# if tot == 2:
#    print(f'O numero {n} é um numero primo.')
# else:
#    print(f'O numero {n} é divisivel por {tot} numeros , ele não é primo.')

# frase = str(input('Escreva uma palavra: ').strip().lower())
# palavra = frase.split()
# pal = ''.join(palavra)
# inverso = ''
# for c in range(len(pal) - 1, -1, -1):
#    inverso += pal[c]
# if pal == inverso:
#    print(f'Temos um palindromo: {pal} e {inverso}')
# else:
#    print(f'Essa frase não tem um palindromo: {pal} e {inverso} ')

# maior = 0
# menor = 0
# for c in range(1, 8):
#    nas = int(input('Diga o ano do seu nascimento: '))
#    mat = 2024 - nas
#    if mat >= 21:
#        maior += 1
#    else:
#        menor += 1
# print(f'Dentre das sete pessoas apenas {maior} atingiram a maturidade, enquanto {menor} ainda não atingiram')

# mapeso = 0
# mepeso = 0
# for c in range (1, 6):
#    peso = float(input(f'Diga o peso da {c}° pessoa: '))
#    if c == 1:
#        mapeso = peso
#        mepeso = peso
#    else:
#        if peso > mapeso:
#            mapeso = peso
#        elif peso < mepeso:
#            mepeso = peso
# print(f'O maior peso foi de {mapeso:.2f}Kg, enquanto o menor foi {mepeso:.2f}Kg.')

# totidade = 0
# idademaisvelho = 0
# homemmaisvelho = ''
# menosdevinte = 0
# for c in range (1, 5):
#    print(f'-=-=-=-=-=-=-=- {c}° PESSOA =-=-=-=-=-=-=-=-=-=')
#    nome = str(input('Diga o seu nome: ').title())
#    idade = int(input('Diga a sua idade: '))
#    sexo = str(input('Você é homem ou mulher: ').title())
#    if c == 1 and sexo in 'Homem':
#        idademaisvelho = idade
#        homemmaisvelho = nome
#    if sexo in 'Homem' and idade > idademaisvelho:
#        idademaisvelho = idade
#        homemmaisvelho = nome
#    if sexo in 'Mulher ' and idade < 20:
#        menosdevinte += 1
#    totidade += idade
# media = totidade / 4
# print(f'A média das idades são de {media:.1f}')
# print('=-' *25)
# print(f'O homem mais velho se chama {homemmaisvelho} e tem {idademaisvelho} anos de idade')
# print('=-' *25)
# if menosdevinte > 1:
#    print(f'E nesse grupo tem {menosdevinte} mulheres com menos de 20 anos')
# else:
#    print(f'E nesse grupo tem {menosdevinte} mulher com menos de 20 anos')

# maisrapido = 0
# nomerapido = ''
# print('------------------------ MEDIDOR DE VELOCIDADE -------------------------')
# for c in range (1, 6):
#    velocidade = int(input('Qual a velocidade maxima que o veiculo atingiu: '))
#    motorista = str(input('Quem estava dirigindo: '))
#    print('--' * 36)
#    if c == 1:
#        maisrapido = velocidade
#        nomerapido = motorista
#    else:
#        if maisrapido < velocidade:
#            nomerapido = motorista
#            maisrapido = velocidade
# print(f'A pessoa mais rapida foi {nomerapido} e atingiu {maisrapido}Km/h')

# nomevelho = ''
# nomenovo = ''
# nomemaislongo = 0
# maisvelho = 0
# maisnovo = 0
# nomedomaislongo = ''
# for c in range(1, 6):
#    print('=-' *28)
#    nome = str(input('Diga o seu nome inteiro: ').title().strip())
#    if c == 1:
#        nomemaislongo = len(nome)
#    else:
#        if len(nome) > nomemaislongo:
#            nomemaislongo = len(nome)
#            nomedomaislongo = nome
#    idade = int(input('Diga a sua idade: '))
#    if c == 1:
#        maisvelho = idade
#        maisnovo = idade
#        nomevelho = nome
#        nomenovo = nome
#    else:
#        if idade > maisvelho:
#            maisvelho = idade
#            nomevelho = nome
#        elif idade < maisnovo:
#            maisnovo = idade
#            nomenovo = nome
# print(f'''O nome mais longo tem {nomemaislongo} letras e é da pessoa chamada {nomedomaislongo}
# e a pessoa mais nova tem {maisnovo} e é a pessoa {nomenovo}
# enquanto a pessoa mais velha tem {maisvelho} e se chama {nomevelho}''')
