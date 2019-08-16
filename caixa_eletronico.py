nome = input('insira seu nome completo: ')
idade = int(input('insira sua idade: '))
saldo = float(input('insira seu saldo: '))

def cond():

    janela = (input('Para Saque(1), \nDepósito(2), \nEmprestimo(3), \nInfo(4), \nSair(outro) \n: '))
    if janela == '1':
        op_saque()

    elif janela == '2':
        op_deposito()

    elif janela == '3':
        op_emprestimo()

    elif janela == '4':
        _info()

    else:
        print('processo finalizado.')

def op_saque(saldo):
    saque = float(input('valor saque: '))
    if saque > 1000 or saque > saldo:
        print('Saque indisponivel')

    else:
        saldo - saque
        print('R$:' + str(saldo))

    cond()


def op_deposito(saldo):
    deposito = float(input('Insira o valor do depósito: '))
    if deposito > 5000:
        print('Valor maximo de depósito é R$ 5000')

    else:
        deposito + saldo
        print('R$:' + str(saldo))

    cond()


def op_emprestimo(saldo):
    emprestimo = float(input('Insira o valor para emprestimo: '))
    if idade < 21:
        print('Emprestimo recusado, por idade inválida.')

    elif saldo <= 1000 and emprestimo < 2000 and emprestimo > saldo*15:
        print('empréstimo recusado')

    else:
        emprestimo + saldo
        print('Emprestimo aprovado.')
        print('R$:' + str(saldo))

    cond()

def _info(saldo):
    print('nome:' + nome, 'idade:' + str(idade), 'saldo: R$ ' + str(saldo))
    cond()

if saldo:
    cond()


