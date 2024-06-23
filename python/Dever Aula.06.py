#from random import randint
#pc: int = randint(0,5)
#jogador = int(input('Tente adivinhar o numero 0 a 5 que eu estou pensando: '))
#if jogador == pc:
#    print(f'Parabens você acertou')
#else:
#    print(f'MUITO RUIM, o numero era {pc}, tente denovo')

#velo = int(input('Diga a velocidade que o carro estava: '))
#if velo >80:
#    multa = float((velo-80)*7.00)
#    print(f'Voce tera que pagar uma multa que sera de {multa:.2f} reais')
#else:
#    print('Você estava dentro do limite de velocidade, siga as leis de transito.')
#print('tenha um bom dia.')

#num = int(input('Diga um numero: '))
#div = num%2
#if div == 1:
#    print(f'O numero que você escolheu é impar, {num}')
#else:
#    print(f'O numero que você escolheu é par, {num}')
#km = float(input('Diga a distancia que deseja percorrer: '))
#if km <= 199:
#    valor = km * 0.50
#    print(f'O valor vai ser de R${valor:.2f}')
#else:
#    valor = km * 0.45
#    print(f'O valor vai ser de R${valor:.2f}')

#ano = int(input('Diga qual ano você quer saber se é bissexto: '))
#resul = ano % 4
#if resul == 0:
#    print(f'O ano {ano} é bissexto.')
#else:
#    print(f'O ano {ano} não é bissexto')

#a = input('Escreva um numero: ')
#b = input('Escreva um numero: ')
#c = input('Escreva um numero: ')
#menor = a
#if b<a and b<c:
#    menor = b
#if c<b and b<a:
#    menor = c
#maior = a
#if b>a and b>c:
#    maior = b
#if c>b and b>a:
#    menor = c
#print(f'O maior valor foi {maior}')
#print(f'O menor valor foi {menor}')

#salario = float(input('Diga o seu salario: '))
#print ('=-'*25)
#if salario > 1250:
#    aumento = salario + (salario * 10 / 100)
#    print(f'O seu novo salario é {aumento}')
#if salario <= 1250:
#    aumento = salario + (salario * 15 / 100)
#    print(f'O seu novo salario é de {aumento}')
#print('=-'*25)

#l1 = float(input('Digite o segmento: '))
#l2 = float(input('Digite o segmento: '))
#l3 = float(input('Digite o segmento: '))
#if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
#    print('É possivel fazer um triangulo com essas medidas')
#else:
#    print('Não é possivel ter um triangulo com essas medidas')
