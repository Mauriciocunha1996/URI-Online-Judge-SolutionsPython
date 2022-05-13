def soma(n1, n2):
    s = n1 + n2
    return s


def diferenca(n1, n2):
    d = n1 - n2
    return d


def divisao(n1, n2):
    d = n1 / n2
    return d


def multiplicacao(n1, n2):
    m = n1 * n2
    return m

def escolha(n):


while True:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print('\t1- Soma: ')
    print('\t2- Diferenca: ')
    print('\t3- Divisão: ')
    print('\t4- Multplicação: ')
    print('\t0- Sair: ')
    escolha = int(input('Escolha: '))
    if escolha == 0:
        break
    if escolha == 1:
        print(f'A soma é {soma(a, b)}')
        continue
    elif escolha == 2:
        d = diferenca(a, b)
        print(f'A diferença é: {d}')
        continue
    elif escolha == 3:
        div = divisao(a, b)
        print(f'A divisão é: {div}')
        continue
    elif escolha == 4:
        mul = multiplicacao(a, b)
        print(f'A multiplicação é: {mul}')
        continue
    else:
        print('Opção incorreta...')
        continue