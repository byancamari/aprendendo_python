from datetime import datetime, timedelta
   
#date 
hoje = datetime.now()
print(hoje.date())

#variações de data 
amanha = hoje + timedelta(days=1)
print(amanha)

#data específica 
data_espe =  datetime(year=2022, month=5,day=20)
diferenca = hoje - data_espe
print(diferenca.days)

#extrair datas 
data = "01/03/2034"
data =  datetime.strptime(data, "%d/%m/%Y")
print(data)

#data no formarto brasileiro
print(hoje.strftime("%d/%m/%Y"))
