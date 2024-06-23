# O if e else são comandos para dar mais opções para o usuario, agr temos o elif, seria um tipo um 'porem', ele pode ser
# usado quantas vezes for preciso, diferente do if q é somente no inicio e do else q é opcional, tbm temos o 'or', que
# seria tipo um 'ou', ex: if (variavel) == (algo) or (variavel) => (algo)

nome = str.title(input('Diga o seu nome: '))
nms = len(nome.split())
if nms == 1:
    print('Nossa o seu nome é só isso??')
elif nms == 2:
    print('O seu nome é bem curto')
elif nms == 3:
    print('Nome de tamanho consideravel')
elif nms == 4:
    print('Você quis todos o nomes do mundo pra você foi?')
else:
    print('CHEGA DE NOME PESSOA')