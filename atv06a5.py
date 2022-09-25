#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos, ambos aplicados aocusto de fábrica.
#Sabe-se que as porcentagens são as mesmas que estão na tabela a seguir. Faça um programa que receba o custo de fabrica de uma carro  mostre o custo ao consumidor.

print('Custo de um carro novo')

valorcar = float(input('Digite o valor do carro: '))

if valorcar <= 12000 :
    res = (valorcar * 1.05)
elif valorcar <= 25000 :
    res = (valorcar * 0.10) + (valorcar * 0.15) + valorcar
else :
    res = (valorcar * 0.15) + (valorcar * 0.20) + valorcar
   
print(f'O valor do carro final é de {res} reais')