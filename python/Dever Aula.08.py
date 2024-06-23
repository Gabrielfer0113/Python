# print('=-'*55)
# print('Ola, eu sou um progama para fazer os seus emprestimos, mas para isso precisamos de umas respostas antes:')
# print('=-'*25)
# sal = int(input('Diga o seu salario: '))
# print('=-'*25)
# imovel = int(input('Diga o valor do imóvel que deseja comprar:'))
# print('=-'*25)
# anos = int(input('Em quantos anos deseja pagar o imóvel: '))
# print('=-'*25)
# mensal = anos*12/imovel
# trin = sal/100*30
# if trin < mensal or trin == mensal:
#    print('O emprestimos sera efetuado, parabens')
# elif trin > mensal:
#    print('Infelizmente não sera possivel fazer essa tranzação,'
#          ' por conta de que 30% do salario não cobre a parcela da divida')
# print('=-'*60)

# n1 = int(input('Digite um numero: '))
# n2 = int(input('Digite um numero: '))
# if n1 > n2:
#    print(f'O primeiro valor é maior: {n1}')
# elif n2 > n1:
#    print(f'O segundo valor é maior: {n2} ')
# elif n1 == n2:
#    print('O resultado são iguais!')

# nas = int(input('Diga o ano que você nasceu: '))
# idade = 2024 - nas
# if idade < 18:
#    alis = nas + 18
#    print(f'\033[31mVocê ainda é de menor, você podera se alistar em {alis}\033[m')
# elif idade == 18 or idade > 18:
#    alis = nas + 18
#    print(f'\033[32mVocê ja é de maior, você poderia ter se alistado em {alis}\033[m')

# nota = float(input('Diga a sua nota: '))
# notaa = float(input('Diga a sua nota: '))
# final = (nota + notaa) / 2
# if final < 5:
#    print(f'Infelizmente você foi reprovado. Média {final}')
# elif 7 > final >=5:
#    print(f'Você esta de recuperação!! Média {final}')
# elif final >= 7:
#    print(f'Você foi aprovado, parabens!! Média {final}')

# idade = int(input('Diga a sua idade: '))
# if idade < 9:
#    print('Sua classificação é: \033[32mMIRIM\033[m')
# elif idade < 14:
#    print('Sua classificação é: \033[32mINFANTIL\033[m')
# elif idade == 19:
#    print('Sua classificação é: \033[32mJUNIOR\033[m')
# elif idade == 20:
#    print('Sua classificação é: \033[32mSENIOR\033[32m')
# else:
#    print('Sua classificação é: \033[32mMASTER\033[32m')

# l1 = float(input('Diga o primeiro segmento da reta: '))
# l2 = float(input('Diga o segundo segmento da reta: '))
# l3 = float(input('Diga o terceiro segmento da reta: '))
# if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
#    print('Esse triangulo é ', end='')
#    if l1 == l2 == l3:
#        print('EQUILATERO')
#    elif l1 != l2 != l3 != l1:
#        print('ESCALENO')
#    else:
#        print('ISOCELES')
# else:
#    print('Não é possivel fazer um triangulo com essas medidas!')
# peso = float(input('Diga o seu peso: '))
# altura = float(input('Diga a sua altura: '))
# imc = peso / altura / altura
# if imc < 18.5:
#    print('Você esta \033[31mABAIXO DO PESO\033[m.')
# elif imc < 25 or imc == 25:
#    print('Você esta no \033[32mPESO IDEAL\033[m')
# elif imc < 30 or imc == 30:
#    print('Você esta \033[31m\033[33mACIMA DO PESO\033[m')
# elif imc < 40 or imc == 40:
#    print('Você esta com \033[31mobesidade\033[m')
# else:
#    print('\033[31mVOCÊ ESTA COM OBESIDADE MORBIDA\033[m')

# print('=-'*15, 'CONVERSOR BINARIO, OCTAL E HEXADECIMAL', '=-'*15)
# n = int(input('Digite um numero inteiro: '))
# op = print('''Escolha uma das bases abaixo
# [1] \033[34mBINARIO\033[m
# [2] \033[34mOCTAL\033[m
# [3] \033[34mHEXADECIMAL\033[m''')
# esco = int(input())
# if esco == 1:
#    print(f'O valor de {n} em \033[32mBINARIO\033[m é {bin(n)}'[2:])
# elif esco == 2:
#    print(f'O valor de {n} em \033[32mOCTAL\033[m é {oct(n)}'[2:])
# elif esco == 3:
#    print(f'O valor de {n} em \033[32mHEXADECIMAL\033[m é{hex(n)}'[2:])
# elif esco > 3:
#    print('\033[31mEsse resultado não existe na tabela acima!!!\033[m')

# produto = float(input('Digite o valor do produto: '))
# print(''' Nossa loja oferece descontos a partir da forma de pagamento
# [1] A vista
# [2] parcelado''')
# esco = int(input(''))
# if esco == 1:
#    print('''O pagamento sera no:
#    [1]CARTÃO
#    [2]CHEQUE
#    [3]DINHEIRO''')
#    vispa = int(input(''))
#    if vispa == 1:
#        valor = produto-(produto*5/100)
#        print(f'O valor do produto selecionado foi de {produto:.2f} R$ para {valor:.2f} R$')
#    elif vispa == 2 or 3:
#        valor = produto-(produto*10/100)
#        print(f'O valor do produto selecionado foi de {produto:.2f} R$ para {valor:.2f} R$')
# elif esco == 2:
#    print('''obs: caso a parcela seja somente de duas vezes não tera tarifa nenhuma
#    caso seja igual ou mais doque três vezes a parcela tera uma juros de 20%.''')
#    valor = int(input('Em quantas vezes deseja parcelar esse produto: '))
#    if valor == 2:
#        valor = produto/2
#        print(f'O valor a ser pago sera de R${valor:.2f} durante dois mêses.')
#    elif 3 <= valor:
#        preco = produto+(produto*20/100)
#        print(f'O valor sera de R${preco/valor:.2f} por R${valor} meses.E o novo preço com o juros sera de R${preco}')
#print('Tenha um bom dia!!')

from random import randint
jokenpo = 'pedra', 'papel', 'tesoura'
print('-=' * 4)
print('JOKENPO')
print('-=' * 4)
print('''Escolha entre
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador = int(input())
if jogador >= 3:
    print('jogada invalida')
pc = randint(0, 2)
if pc == 0:
    print(f'O computador jogou {jokenpo[pc]}')
    print(f'O jogador jogou {jokenpo[jogador]}')
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('O JOGADOR VENCE!!')
    elif jogador == 2:
        print('O COMPUTADOR VENCE!!')
elif pc == 1:
    print(f'O computador jogou {jokenpo[pc]}')
    print(f'O jogador jogou {jokenpo[jogador]}')
    if jogador == 0:
        print('O COMPUTADOR VENCE!!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE!!')
elif pc == 2:
    print(f'O computador jogou {jokenpo[pc]}')
    print(f'O jogador jogou {jokenpo[jogador]}')
    if jogador == 0:
        print('O JOGADOR GANHA!!')
    elif jogador == 1:
        print('O COMPUTADOR GANHA!!')
    elif jogador == 2:
        print('EMPATE')
