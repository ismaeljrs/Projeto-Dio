'''
Autor: Ismael Jorge Brandão
Data: 20/03/2025
Objetivo: Criar um sistema bancário com operações de saque, depósito e visualização de extrato.
Curso: Projeto Dio

'''

# Depósito, saque, extrato

# Depósito: valores positivos para a conta bancária. O projeto trabalha apenas com 1 usuário.
# Operações de saque: realizar até 3 saques diários, com limite máximo de R$ 500 por saque. Caso o usuário não tenha saldo suficiente, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e a operação de extrato deve exibir esses saques.

# Operações de extrato: essa operação deve listar todos os depósitos e saques realizados na conta. No final da listagem, deve ser exibido o saldo atual da conta. Os valores devem ser exibidos no formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500,45
import os

def titulo():
    print('=='*40)
    print(f'*',' '*26,'BANCO DO BRASIL',' '*26,'*')
    print('=='*40)
    print(' '*20,'Seja bem Vindo! Ao Banco do Brasil',' '*20)
    print('=='*40)

def atendimento():
    print('Como podemos ajuda-lo hoje?')
    print('--'*14)
    print(
        '.1 - Realizar um Dépósito\n'
        '.2 - Realizar um Saque\n'
        '.3 - Consultar Extrato'
    )
    print('--'*14)

def extrato(valor):
    print('=='*40)
    print(' '*26,'EXTRATO BANCARIO',' '*26)
    print('=='*40)
    print('\n')
    print('--'*20)
    print(f'Extrato bancario e R${saldo_cont_usu}') 
    print('--'*20)

limite_saque = 3

#informações do Úsuario
saldo_cont_usu = 4000.0
flag = True
while flag:
    os.system('clear')
    titulo()
    input()
    os.system('clear')
    atendimento()
    try:
        escolha = int(input('Selecione uma opção para continuar: '))
        os.system('clear')
    except:
        print('\n')
        print('=' * 40)
        print(' Erro: Digite apenas Números validos')
        print('=' * 40)
        print('Tente novamente')
        print('-' * 40)
        print('Pressione ENTER para continuar...')
        print('=' * 40)
        input()
        continue

    if escolha == 1:
        print('=='*40)
        print(' '*26,'DEPÓSITO BANCÁRIO ',' '*26)
        print('=='*40)
        try:
            Depositar = float(input('Qual valor deseja Depostitar Hoje? '))
        except:
            print('\n')
            print('=' * 40)
            print(' Erro: Digite apenas Números validos')
            print('=' * 40)
            print('Tente novamente')
            print('-' * 40)
            print('Pressione ENTER para continuar...')
            print('=' * 40)
            input()
            continue
        print('\n')
        print('PROCESSO DO DEPÓSITO...')
        if Depositar >= 500 and saldo_cont_usu >= Depositar:
            saldo_cont_usu -= Depositar
            print('--'*51)
            print(f'Depósito realizado com sucesso! R${Depositar:.2f} foram creditados na sua conta corrente 12345-6, agência 9876.')
            print('--'*51)
        elif Depositar > saldo_cont_usu:
            print('--'*35)
            print('Informando que não será possível sacar o dinheiro por falta de saldo')
            print('--'*35)
        else:
            print('--'*20)
            print('O valor minino de Deposito e R$500,00')
            print('--'*20)

    if escolha == 2:
        print('=='*40)
        print(' '*26,'REALIZANDO SAQUE ',' '*26)
        print('=='*40)
        try:
            Saque = float(input('Qual e valor que deseja sacar? '))
        except:
            print('\n')
            print('=' * 40)
            print(' Erro: Digite apenas Números validos')
            print('=' * 40)
            print('Tente novamente')
            print('-' * 40)
            print('Pressione ENTER para continuar...')
            print('=' * 40)
            input()
            continue
        if limite_saque > 0:
            print('\n')
            print('PROCESSO DO DEPÓSITO...')
            if Saque <= 0:
                print('--'*20)
                print('Valor inválido! O saque deve ser maior que zero.')
                print(f'Limite de Saque: {limite_saque}')
                print('--'*20)
            elif Saque <= saldo_cont_usu:
                saldo_cont_usu -= Saque
                limite_saque -= 1
                print('--'*20)
                print(f'Saque realizado com sucesso! R$ {Saque} debitados da sua conta 12345-6, agência 9876. Saldo atual: {saldo_cont_usu}')
                print(f'Limite de Saque: {limite_saque}')
                print('--'*20)
            else:
                print('Informando que não será possível sacar o dinheiro por falta de saldo')

        else:
            print('-' * 45)
            print('Você atingiu o limite de 3 saques permitidos para hoje. Para mais transações, aguarde o próximo período.')
            print('-' * 45)
    if escolha == 3:
        extrato(saldo_cont_usu)

    print('\n')
    flag1 = True
    while flag1:
        try: 
            sair = str(input('Deseja sair?: S - Sim | N - Não: '))
        except:
            print('\n')
            print('=' * 40)
            print(' Erro: Digite apenas Números validos')
            print('=' * 40)
            print('Tente novamente')
            print('-' * 40)
            print('Pressione ENTER para continuar...')
            print('=' * 40)
            input()
            continue
        if sair.lower() == 's':
            os.system('clear')
            print('=' * 45)
            print('Saindo... Obrigado por utilizar o Banco do Brasil!')
            print('-' * 45)
            print('Pressione Enter para finalizar.')
            print('=' * 45)
            input()
            flag = False
            flag1 = False
        elif sair.lower() == 'n':
            flag1 = False
            
