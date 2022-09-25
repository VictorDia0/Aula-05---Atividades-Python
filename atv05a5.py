n = 0
n1 = 0
x = 0
y = 0

print('Digite um numero negativo para finalizar o programa!')
while x >= 0 :
    x = int(input('Digite o numero:'))  
    if x  < 0 :
        break
    elif x >= 30 and x <= 80 :
        n = n + 1
    else:
        n1 = n1 +1
    y = y + x
media = y / (n1 + n)
print(f'A soma dos numeros é {y}.')
print(f'A media é {media}.')
print(f'A quantidade de numeros entre 30 e 80 é {n} número(s)')
print(f'Os que estão fora do intervalo é {n1}.')