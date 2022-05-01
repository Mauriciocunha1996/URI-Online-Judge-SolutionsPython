x = int(input())
y = int(input())
if x > y:
    aux = x
    x = y
    y = aux
soma = 0
for c in range(x+1,y):
    if c % 2 != 0:
        soma += c
print(soma)
