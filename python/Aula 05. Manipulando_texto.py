ex = ('Gabriel Fernando da Silva')
print(ex[0:26:2])
print(ex[:15])
print(ex[6:])
print(ex[6::3])

# Todas as cadeias de numeros começam com 0, ou seja, a primeira letra que vc escrever vai ser o numero 0.
# Dentro dos colchetes o primeiro numero vai indicar de qual letra vc quer que o progama comece a ler.
# O segundo vai indicar até qual letra vc quer q pare.
# Ja o terceiro vai pular as letras correspondente a quantidade inserida.
# Se não houver numero antes do primeiro dois pontos (:), ele vai considerar que é para começar desde o inicio.
# Caso seja o contrario, ele vai fazer o oposto da de cima.
# Sera a mesma coisa de cima só que vai pular os caracteres apartir do ultimo numero.

print(ex.count('a', 0, 17))
# Nesse caso ele contaria a quantidade de letras selecionadas que estariam dentro das aspas ('').
# Ja os numeros seriam de onde ele deve começar a contar e onde deve parar.
# Caso queira não precisa conter os numeros.

print(len(ex))
# Esse comando conta a quantidade de caracteres dentro da cadeia de letras que for inserida.

print(ex.find(input('Escreva algo que queira achar dentro da frase: ')))
# Ele é usado para achar algo que você queira dentro da frase que esta escrita.

vf = input('Escreva alguma palavra para ver se ela existe na frase acima: ') in ex
print(vf)
# Ele fala se aquela ou aquelas palavras tem na cadeia de palavras

re = ex.replace(input('Escreva qual a palavra que deseja trocar: '), input('Escreva a palavra nova: '))
print(re)
# Você escolhe uma palavra para substir e outra para entrar no local da anterior

print(ex.upper())
print(ex.lower())
# A .upper deixa tudo maiusculo ja a lower deixa tudo minusculo

print(ex.capitalize())
print(ex.title())
# O .capitalize ele deixa somente a primeira letra da frase maiuscula, o .title deixa o inicio de cada palavra maiusculo

print(ex.strip())
# Esse comando serve para retirar espaços adicionais, tipo no começo e no final da frase.São muito usados em sites que requerem login
print(ex.rstrip())
# Nesse caso ele só vai retirar os espaços desnecessarios da parte direita da frase
print(ex.lstrip())
# Ele vai fazer o oposto nesse caso, somente a parte da esquerda

c = ex.split()
print()
# Ele vai dividir as palavras pelos os seus espaços, assim criando varias cadeias a partir de cada palavra, as cadeias vão estar numeradas da esquerda para a direita, começando do numero 0
# print(c[2][2]) Isso faria ver a cadeia 2 e a segunda letra dela
r = '-'.join(c)
print(r)
# Essa função ela é dependente da função split

print("""OLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA MUN
      DOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
      OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO 
      oia q legal""")
