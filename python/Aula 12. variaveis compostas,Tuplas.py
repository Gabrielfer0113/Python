opção = ('pão', 'Salcicha', 'Maionese', 'Ketshup')
# print(opção[1])

# Ele mostra-ra somente o item 'salcicha' por conta dos colchetes com a localização dele, que seria o nome '1'
# A ordem sera da esquerda da direita, do 0 até a quantidade que tiver de itens na Tupla

for lanche in range(len(opção)):
    print('Hoje eu quero comer um', opção[lanche])
    # Esse print sem os colchetes e a var 'lanche' dentro só iria contar a var lanche em forma de numeros
for lanche in range(len(opção)):
    print(lanche)
# Na aula o comando 'sorted' serve para deixar na ordem opósta
print(sorted(opção))
# E temos o comando '.index' ele serve para ver em qual posição um item esta, ex:
num = 1, 8, 5, 9, 6, 7
print(num)
print(num.index(5))

# tambem podemos apagar uma Tupla, nunca altera-la, mas sim apagar ela por inteira, ex:
del(num)
print(num)
