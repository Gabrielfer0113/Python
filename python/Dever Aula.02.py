#n1=int(input('Digite um numero:'))
#n2=int(input('Digite um numero:'))
#val=n1+n2
#print('O valor  da soma de {} e {} é de {}'.format(n1,n2,val))

cores = {'limpo' : '\033[m',
         'verde' : '\033[32m',
         'vermelho' : '\033[31m'}
dig = input(('Digite alguma coisa: {}'.format(cores['vermelho'])))
print('Essa frase tem somente letras maiusculas? ', dig.isalpha())
print('Essa frase tem somente letras minusculas? ', dig.islower())
print('Tem espaços nessa frase? ', dig.isspace())
print('Esse caracter é um digito? ', dig.isdigit())
print('Essa frase é somente letras maiusculas? ', dig.isupper())
print('Isso é um numero? ', dig.isnumeric())
print('Esse numero é um decimal? ', dig.isdecimal())
print('Esse digito é um numero? ', dig.isalnum())
print('O tipo desse numero é da ', type(dig))
