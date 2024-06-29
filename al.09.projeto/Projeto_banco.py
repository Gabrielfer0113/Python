from os import system
from time import sleep

rs, saldo, retirar = float(0), float(0), float(0)
saques_dia, esco = int(0), int(0)
extrato = str("")

def linha():
    print("-------------------------------------------------------------")


while True:
    system("cls")
    linha()
    print("""
    PROJETO BANCO\n
    [1] DEPÓSITO
    [2] SAQUE
    [3] EXTRATO
    [4] FINALIZAR PROGRAMA
            """)
    linha()
    esco = int(input("Digite a operação que deseja realizar: "))
    linha()
    if esco == 1:
        while True:
            rs = float(input("Digite o quanto deseja armazenar: "))
            if rs <= 0:
                linha()
                print("Digite um valor que seja maior que R$ 0.00")
                linha()
            else:
                extrato += (f"Depósito R$ {rs}\n")
                saldo += rs
                break
    elif esco == 2:
        saques_dia += 1
        while True:
            retirar = float(input("Digite o quanto deseja sacar: "))
            if saques_dia > 3:
                print("""
Não sera possivel realizar mais um saque,
o limite diario é de três vezes ao dia.
                  """)
                sleep(4)
                break
            elif saldo < retirar:
                print("O saldo é menor que o valor que deseja retirar, tente novamente.")
            elif retirar > 500:
                print("O saque não pode ser maior que R$ 500.00 ")
            elif retirar <= 0:
                print("O saque não pode ser menor que R$ 0.00")
            else:
                extrato += f"Saque R$ {retirar:.2f}\n"
                saldo -= retirar
                break
    elif esco == 3:
        print("------------------= Extrato =-----------------")
        print(f"Nenhuma movimentação foi realizada." if not extrato else extrato)
        print(f"Saldo R$ {saldo:.2f}")
        sleep(10)
    
    elif esco == 4:
        print("Finalizando o programa.")
        sleep(4)
        break

    else:
        print("Opção invalida, tente novamente")
        sleep(3)
        