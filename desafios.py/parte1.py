#001 Ask for the user’s first name and display the output message Hello [First Name] .  
#001 Peça o primeiro nome do usuário e exibir a mensagem de saída Olá [Nome].
fist_name=input('Digite o seu primeiro nome')
print('Olá',fist_name)

#002 Ask for the user’s first name and then ask for their surname and display the output message Hello [First Name] [Surname]. 
#002 Peça o primeiro nome do usuário e, em seguida, peça seu sobrenome e exibir a mensagem de saída Olá [Nome] [Sobrenome].
fist_name_=input('Digite seu primeiro nome')
Sur_name= input('Digite seu sobrenome')

#003 Write code that will display the joke “What do you call a bear with n teeth?” and on the next line display the answer “A gummy bear!” Try to create it using only one line of code.
#003 Escreva um código que exibirá a piada “O que você chama de urso sem dentes?" e na próxima linha exiba a resposta “Um ursinho de goma!” Tente criá-lo usando apenas uma linha de código.
print('O que você chama de urso sem dentes?\nUm ursinho de goma!')

#004 Ask the user to enter two numbers. Add them together and display the answer as The total is [answer]. 
#004 Peça ao usuário para entrar dois números. Adicionar eles juntos e exibir a resposta como O total é [responda].
number_one=int(input('Digite um número'))
number_two= int(input( 'Digite outro número'))
resultado = number_one + number_two
print(resultado)
#teste
#005 Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. Display the answer as The answer is [answer]
#005 Peça ao usuário para inserir três números. Junte o primeiro dois números e depois multiplique este total pelo terceiro. Exibem o responda como A resposta é [responda]
number_one=int(input('Digite o primeiro número'))
number_two=int(input('Digite o segundo número'))
number_three=int(input('Digite o terceiro  número'))
resul = (number_one + number_two) * number_three
print('A resposta é', resul)

#006 Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a userfriendly format
#006 Pergunte quantas fatias de pizza o usuário começou e pergunte quantas fatias Eles comeram. Calcule quantos fatias que eles deixaram e exibir 
fat_inicial= int(input('Quantas fatias existiam no começo?'))
fat_com= int(input('Quantas fatias você comeu?'))
fat_final = fat_inicial - fat_com
print('Fatias existentes no momento', fat_final)

#007 Ask the user for their name and their age. Add 1 to their age and display the output [Name] next birthday you will be [new age]
#007 Pergunte ao usuário seu nome e sua idade. Adicione 1 à sua idade e exibir a saída [Nome] no próximo aniversário que você será [nova era]
name = input('Digite seu nome')
idade= int(input('Quantos anos você tem?'))
idade_futura= idade + 1 
print(name,',no seu próximo aniverário você completará',idade_futura,'anos' )

#008 Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by th number of diners and show how much each person must pay. 
#008 Pergunte o preço total da conta e, em seguida, pergunte como muitos comensais existem. Divida o total da conta pelo número de comensais e mostre quanto cada pessoa deve pagar.
conta= int(input('Qual o valor da conta?'))
pessoas = int(input ('Quantas pessoas irão dividir a conta?'))
valor_por_pessoa = conta/ pessoas
print('O valor da conta vai ser de', valor_por_pessoa, 'para cada um!')

#009 Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days. 
#009 Escreva um programa que vai pedir um número de dias e então vai mostre quantos horas, minutos e segundos são nesse número de dias.
dias = int(input('Digite o número de dias'))
horas = dias * 24
minutos = dias * 1440
segundos = dias * 86400
print (dias, 'tem', horas, 'horas,', minutos,'minutos e ', segundos,'segundos')

#010 There are 2,204 pounds in a kilogram. Ask the user to enter a weight in kilograms and convert it to pounds. 
#010 Existem 2.204 libras em um quilograma. Pedir ao usuário inserir um peso em quilogramas e convertê-lo para libras.
peso= int(input('Adicione o peso em quilogramas'))
libras = peso*2204
print(peso,'quilogramas', 'é igual a', libras, 'libras')

#011 Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format. 

number_1 = int(input('Insira um número  maior que 100: '))
number_2 = int(input('Insira um número  abaixo de 10: '))
div= number_1 // number_2
print ("dentro do numero", number_1,"cabem", div, "vezes esse valor" )

#teste