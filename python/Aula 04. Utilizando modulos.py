#import bebida:Vai importar todas as coisas da biblioteca bebida
#from doce import pudim: Você importa somente coisas que você queira

import math
n=float(input('Digite um numero: '))
ra= math.sqrt(n)
print('A raiz de {} é {:.2f }'.format(n,ra))

#from math import sqrt
#n=float(input('Digite um numero: '))
#print('A raiz de {} é {:.2f}'.format(n, sqrt(n)))

#from math import floor
#n=float(input('Digite um numero quebrado: '))
#print('Esse seria ele caso fosse inteiro {}'.format(floor (n)))
