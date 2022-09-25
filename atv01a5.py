#Crie um algoritmo que leia um conjunto de 20 números inteiros e mostre qual foi o maior e menor valor fornecido

n = 0
maior = -1
menor = 1000000 
while n <= 20 :
    Num = int(input('Digite um numero: '))
    if (Num > maior) :
        maior = Num
    if Num < menor :
        menor = Num
    n = n +  1
print(maior,menor)