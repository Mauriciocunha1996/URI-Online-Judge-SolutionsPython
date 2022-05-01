salario = float(input(''))

if 0 <= salario <= 400.00:
    novo_salario = (salario * (15/100)) + salario
    reajuste = (salario * (15/100))
    em_percentual = 15
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: {em_percentual} %')

elif 400.01 <= salario <= 800.00:
    novo_salario_2 = (salario * (12 / 100)) + salario
    reajuste_2 = (salario * (12 / 100))
    em_percentual_2 = 12
    print(f'Novo salario: {novo_salario_2:.2f}')
    print(f'Reajuste ganho: {reajuste_2:.2f}')
    print(f'Em percentual: {em_percentual_2} %')

elif 800.01 <= salario <= 1200.00:
    novo_salario_3 = (salario * (10 / 100)) + salario
    reajuste_3 = (salario * (10 / 100))
    em_percentual_3 = 10
    print(f'Novo salario: {novo_salario_3:.2f}')
    print(f'Reajuste ganho: {reajuste_3:.2f}')
    print(f'Em percentual: {em_percentual_3} %')

elif 1200.01 <= salario <= 2000.00:
    novo_salario_4 = (salario * (7 / 100)) + salario
    reajuste_4 = (salario * (7 / 100))
    em_percentual_4 = 7
    print(f'Novo salario: {novo_salario_4:.2f}')
    print(f'Reajuste ganho: {reajuste_4:.2f}')
    print(f'Em percentual: {em_percentual_4} %')

else:
    novo_salario_5 = (salario * (4 / 100)) + salario
    reajuste_5 = (salario * (4 / 100))
    em_percentual_5 = 4
    print(f'Novo salario: {novo_salario_5:.2f}')
    print(f'Reajuste ganho: {reajuste_5:.2f}')
    print(f'Em percentual: {em_percentual_5} %')
