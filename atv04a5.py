n = 0
z = 0
for i in range (0,10) :
    x = int(input())
    if (x >= 20 and x <= 55) :
        n = n + 1
    z = z + x 
print(f'A quantidade de números que estão no intervalo entre 20 e 55 são {n} numeros.')
print(f'A soma dos números é {z} ')