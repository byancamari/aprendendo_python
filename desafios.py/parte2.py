#teste

class Teste:
    def __init__(self, teste):
        self.teste = teste
    
    def i(self):
        return self.teste

instance = Teste('teste')
print(instance.i())

#012 Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number otherwise show the first number first and then the second.
#012 Peça dois números. Se o primeiro é maior do que o segundo, exibir o segundo número primeiro e, em seguida, o primeiro número, caso contrário, mostrar o primeiro número primeiro e depois o segundo.
num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))
if num1 > num2:
    print(num2,num1)
else:
    print(num1,num2)

#013 Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message “Too high”, otherwise display “Thank you”.
#013 Peça ao usuário para inserir um número que está abaixo 20. Se eles entrarem em um número que é 20 ou mais, exiba o mensagem "Muito alto", caso contrário, exibir "Obrigado".
number = int(input('Insira um número: '))
if number >=20:
    print('Muito alto!')
else:
    print('Obrigada')

#014 Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer”.
#014 Peça ao usuário para inserir um número entre 10 e 20 (inclusive). Se eles inserirem um número dentro deste intervalo, exibir a mensagem "Obrigado você", caso contrário, exiba o mensagem "Incorreto resposta".
number = int(input("Insira um número entre 10 e 20: "))
if number >= 10 and number <=20:
    print('Obrigado você')
else:
    print('incorreto')

#015 Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red
#015 Peça ao usuário para inserir sua cor favorita. Se eles digitarem "vermelho", "VERMELHO" ou "Vermelho" exibir a mensagem "Eu gosto de vermelho também", caso contrário, exibir a mensagem "Eu não gosto [de cor], prefiro o vermelho
cor = input('Qual sua cor favorita?')
if cor =='vermelho' or cor=='VERMELHO':
    print ('Eu também gosto de vermelho')
else:
    print ('Eu não gosto de',cor,',prefiro vermelho')

#016  Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they type it in. If they answer “yes”, ask if it is windy. If they answer “yes” to this second question, display the answer “It is too windy for an umbrella”, otherwise display the message “Take an umbrella”. If they did not answer yes to the first question, display the answer “Enjoy your day”.
#016  Pergunte ao usuário se está chovendo e converta sua resposta para minúsculas então não importa em que caso eles digitam. Se eles responderem "sim", pergunte se está ventando. Se responderem "sim" a esta segunda pergunta, exibir a resposta "Está muito ventoso para um guarda-chuva", caso contrário, exibir a mensagem "Pegue um guarda-chuva". Se não responderam sim para a primeira pergunta, exiba a resposta "Aproveite o seu dia".
resposta = input('Está chovendo? ')
resposta = str.lower(resposta)
if resposta == 'sim':
    ventoso = input('Está ventando? ')
    ventoso = str.lower(ventoso)
    if ventoso =='sim':
      print('Está muito ventoso para um guarda-chuva')
    else:
        print('Pegue um guarda-chuva')
else:
    print('Aproveite seu dia de sol')

#017 Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, display the message “You can learn to drive”, if they are 16, display the message “You can buy a lottery ticket”, if they are under 16, display the message “You can go Trickor-Treating
#017 Pergunte a idade do usuário. Se eles têm 18 anos ou mais, exiba o mensagem "Você pode votar", se eles têm 17 anos, exibir o mensagem "Você pode aprender a drive", se eles são 16, exibir a mensagem "Você pode comprar um bilhete de loteria", se forem com menos de 16 anos, exiba o mensagem "Você pode ir Trickor-Treatingidade 
idade = int(input('Quantos anos você tem? '))
if idade >= 18:
    print('Você já pode votar')
elif idade ==17:
    print('Você pode aprender a dirigir')
elif  idade ==16:
    print('Você pode comprar um bilhete na loteria')
else:
    print('Doces ou travessuras?')

#018 Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, display “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”.
#018 Peça ao usuário para inserir 1, 2 ou 3. Se eles inserirem um 1, exibir a mensagem "Obrigado", se eles digitarem um 2, exibir "Bem feito", se eles digitarem um 3, exiba "Correto". Se eles inserem qualquer outra coisa, exibir "Mensagem de erro".
number = int (input('Insira um núemro de 1 a 3: '))
if number=='1':
    print('Obrigado')
elif number =='2':
    print('Bem feito')
elif number ==3:
    print('Correto')
else:
    print('Mensagem de erro')

#019 Ask the user to enter their first name and then display the length of their name.
#019 Peça ao usuário para inserir seu primeiro nome e em seguida, exiba o comprimento do seu nome
name = input('Insira seu nome: ')
cacteres = len(name)
print(cacteres)

#020 Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space between and display the name and the length of whole name.
#021 Peça ao usuário para inserir seu primeiro nome e, em seguida, peça-lhe para digite seu sobrenome. Junte-os com um espaço entre e exibir o nome e o comprimento do nome inteiro.
first_name = input('Insira seu primeiro nome: ')
last_name  = input('Insira seu sobrenome: ')
name = first_name +"" + last_name 
caracteres = len(name)
print(name, caracteres)

#021 Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result.
#021 Peça ao usuário para inserir seu nome e sobrenome em parte e junte-as. Altere o caso para maiúsculas e minúsculas. Exiba o resultado finalizado.
name1 = input('Insira seu primeiro nome: ')
name2 = input('Insira seu segundo nome: ')
name1 = name1.title()
name2 = name2.title()
print( name1, name2)

#022 Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a starting number and an ending number and then display just that section of the text (remember Python starts counting from 0 and not 1). 
#022 Peça ao usuário para digitar o primeiro linha de uma rima de berçário e exibir o comprimento da cadeia de caracteres. Peça um número inicial e um número final e, em seguida, exibir apenas essa seção do texto (lembre-se Python começa contando de 0 e não 1). 
rima = input('Insira a rima: ')
comprimento = len(rima)
print ('Essa rima tem', comprimento,'letras')
inicio =int(input('Insira um número inicial: ')) 
fim = int(input('Insira um número final: '))
parte = (rima [inicio:fim])
print(parte)

#023 Ask the user to type in any word and display it in upper case. 
#023 Peça ao usuário para digitar qualquer palavra e exibi-la em letra maiúscula.
palavra = input('Digite uma palvra: ')
palavra = palavra.upper()

#024  Ask the user to enter their first name. If the length of their first name is under five characters, ask them to enter their surname and join them together (without a space) and display the name in upper case. If the length of the first name is fiveor more characters, display their first name in lower case.
#024 Peça ao usuário para inserir seu primeiro nome. Se o comprimento de seu primeiro nome é inferior a cinco caracteres, pergunte eles para digitar seu sobrenome e se juntar a eles juntos (sem espaço) e exibir o nome em maiúsculas. Se o comprimento do primeiro nome for cinco ou mais caracteres, exibir seu primeiro nome em minúsculas.
first_name = input('Insira seu primeiro nome: ')
if len(first_name)< 5:
    last_name = input('Insira seu segundo nome: ')
    name = first_name + " " + last_name
    print(name.upper())
else:
    print(first_name.lower())

#025 Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. If a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and change it into Pig Latin. Make sure the new word is displayed in lower case.
#025 O latim porco toma a primeira consoante de uma palavra, move-o para o final da palavra e adiciona um "ay". Se uma palavra começa com uma vogal, basta adicionar "caminho" para o fim. Por exemplo, porco torna-se igpay, banana torna-se ananabay, e aadvark torna-se aadvarkway. Crie um programa que solicitará o usuário para inserir uma palavra e alterá-la para Pig Latin. Verifique se a nova palavra é exibida em minúsculas.
palavra = input ('Insira uma palavra: ')
primeira = palavra[0]
comprimento = len(palavra)
rest = palavra [1:comprimento]
if primeira != 'a' and primeira != 'e' and primeira != 'i' and primeira != 'u':
    nova_palavra = rest + primeira + "ay"
    print(nova_palavra.lower())





