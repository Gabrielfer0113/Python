cores = {'limpo ': '\033[m',
         'vermelho ': '\033[31m',
         'verde ': '\033[32m',
         'amarelo ': '\033[33m',
         'azul ': '\033[34m',
         'roxo ': '\033[35m',
         'ciano ': '\033[36m',
         'cinza ': '\033[37m'}

# nome = input('Diga o seu nome: ')
# print(cores['verde '], nome.upper(), cores['limpo '])
# print(cores['verde '], nome.lower(), cores['limpo '])
# nome1 = nome.split()
# nome2 = ''.join(nome1)
# print(cores['amarelo '], len(nome2), cores['limpo '])

# n = str(input('Digite um numero de 4 caracteres: '))
# n1 = ''.join(n)
# print(n1[0], cores['azul '], ' Milha/s ', cores['limpo '])
# print(n1[1], cores['ciano '], ' Centena/s', cores['limpo '])
# print(n1[2], cores['amarelo '], ' Dezena/s', cores['limpo '])
# print(n1[3], cores['roxo '], ' Unidade/s', cores['limpo '])

# f = str.title(input('Diga o nome de sua cidade: '))
# c = f.split()
# ''.join(c)
# vof = (c[0])
# if vof == 'Santos':
#    print('A sua cidade tem santos no primeiro nome.')
# else:
#    print('A sua cidade não tem santos no primeiro nome.')

# silva = 'Silva'
# nome = str.title(input('Diga o seu nome: '))
# nome2 = silva in nome
# if nome2 == True:
#    print('O seu nome tem', cores['verde '] ,'Silva.')
# else:
#    print('O seu nome não contem', cores['vermelho '] ,'Silva')

# n = str.title(input('Digite qualquer palavra: '))
# a = n.count('a')
# A = n.count('A')
# s = a + A
# print('Essa é a quantidade de letras a, A existentes na sua frase ', cores['verde '], s, cores['limpo '])
# c1 = ''.join(n)
# print('Essa é a posição da primeira vez que a letra a aparece ', cores['azul '], n.find('a'), cores['limpo '])
# print('Essa é a posição da primeira vez que a letra A aparece ', cores['cinza '], n.find('A'), cores['limpo '])
# print('Essa é a ultima posição que a letra a aparece ', cores['ciano '], n.rfind('a'), cores['limpo '])
# print('Essa é a ultima posição que a letra A aparece ', cores['vermelho '], n.rfind('A'), cores['limpo '])

nome = str.title(input('Diga o seu nome: '))
cort = nome.split()
posi = (len(cort)-1)
print('O seu nome é', cores['roxo '], f'{nome}', cores['limpo '])
print('O primeiro nome é', cores['vermelho '] ,f'{cort[0]}', cores['limpo '])
print('O ultimo nome é', cores['azul '] ,f'{cort[posi]}', cores['limpo '])
