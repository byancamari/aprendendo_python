#condição e comparação 
let= 16
if let >=16:
    print('olá mundo')
#caso let seja maior ou igual a 16 será exibido na tela a mensagem 'olá mundo'
en = 28/2*10
if en >=140:
    print('Happy')
#se en for maior ou igual a 140 será exibido na tela a mensagem 'Happy'

#desafio 1
    nota=int(input('Qual sua nota?'))
if nota >=7:
    print('Você foi aprovado!')
elif nota == 6:
  print ('Você foi aprovado por ser participativo!')
else: 
  print ('Você foi reprovado!')
#desafio 2 
  meses=int(input('Quantos meses o Tiago trabalhou?'))
if meses >=12:
    print('Tiago pode tirar férias!')
elif meses == 11:
  print ('Tiago não pode tirar férias, aos menos que  ele trabalhar mais 1 mês ')
else: 
  print ('Sem férias!')
  #desafio 3 
  grau = int(input(' Quantos graus ?'))
if grau > 25:
  print('Oba! A PDA pode marcar a data')
elif grau == 25:
  print('Vamos! O que vale é a companhia')
elif grau <= 15:
  print('Estará muito frio, não podemos alugar nessa data')
else:
    print('Vamos congelar') 
    #desafio 4
    number = int(input('Insira um  número: '))
if number >0:
    print('Número positivo!')
elif number ==0:
    print('Número neutro!')
else:
    print('Número negativo!')
    #desafio 5
    idade= int(input("Digite sua idade: "))
peso= int(input("Digite seu peso: "))
sono = int(input("Digite quantas horas você dormiu nas últimas 24 horas:  "))
if idade >=16 and peso>=50 and sono>=6:
  print("Você pode doar sangue! ")
else:
    print("Você não pode ser um doador!")
    
