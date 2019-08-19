print('\nBANCO INTERNACIONAL')

nome = input('\nInsira seu nome completo para continuar: ').title()
idade = int(input('Olá ' + nome.split()[0] + ', pode nos informar sua idade: '))
saldo = 0


def op_saque(nome, idade, saldo):
    saque = float(input('Informe valor do Saque: '))
    if saque > 1000:
        print('Valor maximo de saque R$: 1000.')
    elif saque > saldo:
        print('Saldo indisponivel.')
        print('SALDO: R$: ' + str(saldo))
    else:
        saldo = saldo - saque
        print('VALOR SAQUE: R$:' + str(saque))
        print('SALDO TOTAL: R$:' + str(saldo))

    return cond(nome, idade, saldo)


def op_deposito(nome, idade, saldo):
    deposito = float(input('Insira o valor do depósito: '))
    if deposito > 5000:
        print('Valor maximo de depósito é R$ 5000.')

    else:
        saldo = deposito + saldo
        print('VALOR DEPOSITADO R$:' + str(deposito))
        print('\nSALDO TOTAL R$:' + str(saldo))

    return cond(nome, idade, saldo)


def op_emprestimo(nome, idade, saldo):
    if idade < 21:
        print('Emprestimo recusado, por idade inválida.')
        return cond(nome, idade, saldo)

    emprestimo = float(input('Insira o valor para emprestimo: '))


    if saldo <= 1000 or emprestimo < 2000 or emprestimo > saldo*15:
        print('Empréstimo recusado.')

    else:
        saldo = emprestimo + saldo
        print('Emprestimo aprovado.')
        print('VALOR EMPRESTIMO R$:' + str(emprestimo))
        print('\nSALDO TOTAL R$:' + str(saldo))

    cond(nome, idade, saldo)

def _info(nome, idade, saldo):
    print('NOME:' + nome, ', IDADE:' + str(idade), ', SALDO: R$ ' + str(saldo))
    cond(nome, idade, saldo)

def cond(nome, idade, saldo):

    janela = (input('''\nPressione:
                    \nPara Saque(1), 
                    \nDepósito(2),
                    \nEmprestimo(3),
                     \nInfo(4), 
                     \nSair(outro)
                      \n: '''
                    ))

    if janela == '1':
        op_saque(nome, idade, saldo)

    elif janela == '2':
        op_deposito(nome, idade, saldo)

    elif janela == '3':
        op_emprestimo(nome, idade, saldo)

    elif janela == '4':
        _info(nome, idade, saldo)

    else:
        print('processo finalizado.')


cond(nome, idade, saldo)



