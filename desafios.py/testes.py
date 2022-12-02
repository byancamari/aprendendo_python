#inputs para entrada de valores
valorA = float(input('Insira valor A: '))
valorB = float(input('Insira valor b: '))
#definição da função somar
def somar(a,b):
    print(a+b)
#outra teste 
def dizer():
    print(' oi')
#Ivocando a função e passando as variáveis 
somar(valorA, valorB)
dizer()


import pandas as pd 

tabela = pd.read_excel('vendedores.xlsx')
print(tabela)

fat = 0 
for venda in tabela['vendas']:
    fat = fat + venda

    if fat > 30000: 
      print("Batemos a meta")
      break  
