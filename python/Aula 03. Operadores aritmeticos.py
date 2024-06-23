#+=Adição, Ex: 5+2==7
#-=Subtração, Ex: 5-2==3
#*=Multiplição, Ex: 5*2==10
#/=Divisão, Ex: 5/2==2.5
#**=Potencia, Ex:5**2==25
#//=Divisão inteira, Ex: 5//2==2
#%=Resto de divisão, Ex: 5%2==1

#Para fazer uma conta de raiz vc pode fazer assim, 25**(1/2), isso sera a raiz quadrada, caso queira mudar para cubica mude o numero 2 para o 3 e assim por diante
#Comando dos colchetes
nome=input('Olá qual é o seu nome? ')
print('Seja bem vindo {:100}!'.format(nome))
print('Seja bem vindo {:^100}exemplos'.format(nome))
print('Seja bem vindo {:<100}não sei mais oq escrever'.format(nome))
print('Seja bem vindo {:>100}batata'.format(nome))
print('Seja bem vindo {:-^100}!'.format(nome))
print('Seja bem vindo {:->100}pão'.format(nome))
print('Seja bem vindo {:-<100}!'.format(nome))

n1=int(input('Digite um numero:'))
n2=int(input('Digite um numero:'))
a=n1 + n2
s=n1 - n2
m=n1 * n2
d=n1 / n2
p=n1 ** n2
di=n1 // n2
r=n1 % n2
print('A soma é {}, \n a subtração é de {}, a multiplicação é {}, a divisão é {:.2f}'.format(a, s, m, d), end=' ')
print('a potencia é {}, a divisão inteira é {}, e o resto da divisão é de {}'.format(p, di, r))
#O (end=, é feito para a linha continuar no proximo print
#O \n seria o oposto do comando acima, ele corta a linha e manda pra baixo
