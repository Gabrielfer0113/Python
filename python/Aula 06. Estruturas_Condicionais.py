cores = {'limpo' : '\033[m',
         'vermelho' : '\033[31m',
         'verde' : '\033[32m',
         'roxo' : '\033[35m'}

#Os comandos estudados hoje vão ser o if e o else, eles são usados para fazer variaveis
idade = int(input('Qual a sua idade: '))
if idade <=17:
    print(cores['vermelho'],'Você é de menor.', cores['limpo'])
else:
    print(cores['verde'] ,'Você ja é de maior.', cores['limpo'])

#Esse segundo modo é para variaveis mais 'rapidas' por serem curtas
print('Você é de menor.' if idade <=17 else'Você ja é de maior.')

#Esse comando pode ser usado de diversas maneiras
Ga = 'Gabriel'
nome = str.title(input('Diga o seu nome: '))
ver = 'Gabriel' in nome
e = nome
verda = 'Emilly' in e
if ver == True:
    print(cores['vermelho'],'Que nome de filho da puta, gostei', cores['limpo'])
if verda == True:
    print(cores['roxo'] ,'QUE NOME LINDO E MARAVILHOSO, NOME DE UMA DEUSA GREGA', cores['limpo'])
print('É um nome legal.')