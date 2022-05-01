n1, n2, n3 = input('').split(" ")
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
lista = [n1, n2, n3]
ordem_que_foram_digitados = lista
lista.sort(reverse=False)
ordem_crescente = "\n".join(map(str, lista))
print(f'{ordem_crescente}', end='\n\n')
print(n1, n2, n3, sep='\n')





