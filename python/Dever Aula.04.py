cores = {'Limpo' : '\033[m',
         'Verde' : '\033[32m',
         'Vermelho' : '\033[31m',
         'Amarelo' : '\033[33m',
         'Azul' : '\033[34m',
         'Roxo' : '\033[35m',
         'Ciano' : '\033[36m',
         'Cinza' : '\033[37m'}

# from math import hypot
# co = float(input('Digite o valor do cateto oposto: '))
# ca = float(input('Digite o valor do cateto adjacente: '))
# print('O valor da hipotenusa é de', cores['Amarelo'] ,f'{hypot(ca,co):.2f}', cores['Limpo'])

# from math import cos, sin, tan, radians
# n = float(input('Escreva um angulo para descobri o seu seno, cosseno e tangente: '))
# print('O seno de', cores['Amarelo'],f'{n}°', cores['Limpo'] ,'é de', cores['Azul'] ,f'{sin(radians(n)):.2f}', cores['Limpo'],
#      ' O cosseno de', cores['Amarelo'] ,f'{n}°', cores['Limpo'],
#      'é de', cores['Roxo'] ,f'{cos(radians(n)):.2f}',cores['Limpo'],
#      'E a tangente de', cores['Amarelo'] ,f'{n}°', cores['Limpo'] ,f'é de {tan(radians(n)):.2f}',cores['Limpo'])

from random import shuffle
print('diga o nome de quatro alunos: ')
a = str(input())
b = str(input())
c = str(input())
d = str(input())
s = [a,b,c,d]
shuffle(s)
print(f'O aluno sorteado foi {s}')
shuffle(s)
print(f'O aluno sorteado foi {s}')

#import pygame
#pygame.init()
#pygame.mixer.music.load("Dever_Aula04.mp3")
#pygame.mixer.music.play()
#input()
#pygame.event.wait()
