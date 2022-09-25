#Um banco concederá um crédito especial aos seus clientes de acordo com o saldo medio no último ano. Façã um programa que receba o saldo médio de um cliente e calcule o valor do crédito, de acordo com a tabela a seguir. MOstre o saldo médio e o valor do credito.

#Saldo médio ----- Percentual
#Acima de R$ 400,00 ----30% do saldo médio
#R$ 400,00 -- R$ 300,00 ----25% do saldo médio
#R$ 300,00 -- R$ 200,00 ----20% do saldo médio
#Até 200,00 ----- 10% do saldo médio

print('Digite abaixo o valor do saldo médio abaixo!!!')
cliente = str(input('Digite seu nome: '))
sm = float(input('Digite o valor: '))
if sm > 0 :
    if sm > 400 :
        credito = sm * 0.30
    elif sm > 300 :
        credito = sm * 0.25
    elif sm > 200 :
        credito = sm * 0.20
    else :
        credito = sm * 0.10    
    print(f'{cliente}, o seu saldo médio é {sm}reais, o valor do crédito é {credito} reais')
elif sm == 0 :
    print(f'{cliente}, você está sem saldo')
else :
    print(f'{cliente}, você está com o saldo negativo')