#INTERACTIVE HELP
#No python temos um comando chamado "help()", ele serve para perguntar uma função do python, mas vc usaria o terminal pra escrever

#DOCSTRINGS
def contador(i, f, p):
    """
    -> faz uma contagem e mostra na tela-
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função crida por Gabriel Fernando, estudante de programação
    """
    c = i
    while c <= f:
        print(f'{c}', end=' - ')
        c += p


help(contador)

#As docstrings seriam a documentação do parametro usado, demos o ex. no comando "def" a cima



#PARAMETROS OPCIONAIS
def somar(a, b, c=0):
    s = a + b + c
    print(f'{s}')

somar(3, 2, 3)
somar(3, 2)


#ESCOPO DE VARIAVEIS // ESCOPO
def teste(n):
    #global n // Esse comando faz que a variavel "n" vai ser global
    x = 8
    n = 5
    print(f"Na função teste, n vale {n}") #dentro da função o "n" vai valer 5
    print(f'Na função teste, x vale {x}')


n = 2
teste(n)
print(f'No programa principal, n vale {n}') #No programa principal o "n" vai valer 2
# print(f'No programa principal, x vale {x}') #Essa variavel não ira valer por conta de ser uma variavel local "x", ele esta dentro da def, ou seja, local


#RETORNO DE VALORES // return

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s #Com esse comando vc retorna o valor da variavel "s" para a variavel "v1/v2/v3", fazendo a variavel local meio que sair do escopo local

v1 = soma(3, 2, 5)
v2 = soma(3, 2, 9)
v3 = soma(3, 2)

print(f'A soma dos valores {v1} + {v2} + {v3} deram {v1 + v2 + v3}')


