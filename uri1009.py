nome = input('')
salario_fixo = float(input(""))
total_vendas = float(input(""))

comissao = total_vendas*(15/100)
salario_com_bunus = comissao + salario_fixo

print(f"TOTAL = R$ {salario_com_bunus:.2f}")

