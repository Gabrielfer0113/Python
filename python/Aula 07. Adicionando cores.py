    #Estilo: 0 = Normal
    #        1 = Negrito
    #        4 = sublinhado
    #        7 = negativo
    #Cor do texto = 30 = branco
    #               31 = vermelho
    #               32 = verde
    #               33 = amarelo
    #               34 = azul
    #               35 = roxo
    #               36 = ciano
    #               37 = cinza
    #Cor do fundo do texto = 40 = branco
    #                        41 = vermelho
    #                        42 = verde
    #                        43 = amarelo
    #                        44 = azul
    #                        45 = roxo
    #                        46 = ciano
    #                        47 = cinza
    #\033[xx;xx;xxm
cores = {'limpo' : '\033[m',
         'vermelho' : '\033[31m',
         'verde' : '\033[32m'}
con = str(input('Qual é o seu nome? '))
print('O seu nome é', cores['vermelho'], f'{con}')
