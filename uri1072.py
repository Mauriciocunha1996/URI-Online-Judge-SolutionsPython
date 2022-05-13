n = int(input(''))
cont = 0
c = 0
out = 0
while cont < n:
    x = int(input(''))
    if 10 <= x <= 20:
        c += 1
    else:
        out += 1
    cont += 1

print(f'{c} in')
print(f'{out} out')