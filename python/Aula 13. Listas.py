# LISTA SÃO MUTAVEIS
# Nós temos Uma 'Tupla', só q diferente dela a gnt usa os colchetes aos inves dos parenteses '[]'
# Nas listas podemos modificar suas variaveis, Ex:
lista = ['mussarela', 
         'pão', 
         'leite', 
         'toddy']

# Temos os comando para adicionar mais variaveis ou substituir a essa lista, ex:
lista[1] = ['maionese'] # Usamos esse comand para substituir um elemento
lista.append('salsicha') # Esse comando vai adicionar na ultima posição, ou seja, na direita
lista.insert(0,'sorvete') # Nesse caso ele toma uma posição e passa tudo pra frente

# E temos como apagar variaveis dessa lista, como:
del lista[0]
lista.pop() # O pop é mais ultilizado para retirar o ultimo valor da lista de variaveis
lista.remove('leite') # Esse funciona na base da escrita
print(lista)

# O proprio programa pode criar lista apartir doq o usuario deseja, ex:
valores = list(range(5,10))
print(valores)
num = [5,4,9,7,8,6,3]
num.sort() # Esse comando organiza em ordem crescente so numeros
print(num)
num.sort(reverse=True) # Nesse caso ele faria em order decrescente
print(num)
for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}')
a = [2, 3, 4, 5]
b = a
b[2] = 7 # Nesse modo a variavel A e B estão interligadas, fazendo assim qualquer
         # modificação na B acontece na A, e vice e versa
print(f'Lista A: {a}',f'\nLista B: {b}') 
b = a[:]
b[2] = 1
print(f'Lista A: {a}', f'\nLista B: {b}')