lista = []
# Eu tenho 2 maneiras de declarar um dicionario
ex1 = dict()
ex2 = {}
ex3 = {'nome': 'Gabriel ' 'Emilly ' 'Leila', 'sexo': 'Masculino', 'Idade': 18}
print(ex3['nome'])
print(ex3.keys()) #O Keys mostra as o nome das localizações dos objetos
print(ex3.values()) #Ele mostra oq tem dentro da biblioteca
print(ex3.items()) #E esse mostra todos os valores acima
#Eu posso o usar o comando 'del' para deletar um item inteiro na biblioteca
ex3['Peso'] = 81.0        #para adicionar um item na biblioteca eu faço assim
for i, v in ex3.items():
    print(f'{i} = {v}')
#Caso eu queira copiar alguma biblioteca para uma lista eu devo usar o comando '.copy()', ele é equivalente ao '[:]'
lista.append(ex3.copy) #dessa maneira