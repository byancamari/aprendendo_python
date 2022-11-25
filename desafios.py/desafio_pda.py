mes = input("Qual o número do mês?")
meses = {"1": "January", "2": "February", "3": "March", 
         "4": "April", "5": "May", "6": "June", 
         "7": "July", "8": "August", "9": "September", 
         "10": "October", "11": "November", "12": "December"}
print(meses[mes])

# DESAFIO 2
tweeter = {"280": "Tweet"}
tweeter = int(input("Quantas caracteres ?"))
if tweeter > 281:
    print("Esse texto é maior que o esperado")
elif tweeter <= 280:
    print("Tweet aceito")

# DESAFIO 3
idade= int(input("Digite sua idade: "))
peso= int(input("Digite seu peso: "))
sono = int(input("Digite quantas horas você dormiu nas últimas 24 horas:  "))
if idade >=16 and peso>=50 and sono>=6:
  print("Você pode doar sangue! ")
else:
    print("Você não pode ser um doador!")
