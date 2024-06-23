# nome=input('Qual é o seu nome:')
# print('Boas vindas ',nome)

# dia=input('Qual dia que você nasceu: ')
# mes=input('Qual mês você nasceu: ')
# ano=input('Qual o ano que você nasceu: ')
# print('A sua data de nascimento é',dia ,'/',mes,'/',ano)

cores = {'limpo' : '\033[m',
        'sublinhadoverde' : '\033[4;32m',
         'ciano' : '\033[36m'}


n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
valor = n1+n2
print('O valor de {}{}{} mais {}{}{} é de {}{}{}'.format(cores['sublinhadoverde'], n1, cores['limpo'],
    cores['sublinhadoverde'], n2, cores['limpo'], cores['ciano'], valor, cores['limpo']))
