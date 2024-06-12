#numero1 = int (input('Digite um número: '))

#numero2 = int (input('Digite mais um número: '))

#divisao = numero1 / numero2

#if numero1 and numero2 != 0:
    #print('A divisão entre esses números é igual a',divisao)

#else:
    #print('Digite um número diferente de 0!')

##----------------------------------------------------------------------------------------------


##numeroA = int(input('Digite o valor de A: '))

##numeroB = int(input('Digite o valor de B: '))

##numeroC = int(input('Digite o valor de C: '))

##if numeroA + numeroB < numeroA + numeroC:
    ##print('A soma entre',numeroA,'+',numeroB,'é menor que',numeroA,'+',numeroC)

##--------------------------------------------------------------------------------------------

##numero = int (input('Digite um número: '))

##triplo = numero * 3

##dobro = numero * 2

##if numero < 0:
    ##print('O triplo desse número é igual a',triplo)

##elif numero > 0:
    ##print('O dobro desse número é igual a',dobro)

##else:
    ##print('Digite um número diferente de 0!')

##------------------------------------------------------------------------------------------------

##num = int (input('Digite um número: '))

##if num % 3 == 0:
    ##print('Esse número é divisível por 3!')

##else:
    ##print('Esse número não é divisível por 3!')

#---------------------------------------------------------------------------------------------------

##num = int (input('Digite um número: '))

##if num % 2 == 0:
    ##print('O número é par!')

##else:
    ##print('O número é ímpar!')

#----------------------------------------------------------------------------------------------------



#aposta = input('Você quer PAR ou ÍMPAR? ')

#numero = input('Digite um número entre 0 e 5: ')

#import random 

#sorteado = random.randint(0,5)


#if (numero + sorteado) %2 == 0 and aposta == 'par':
    #print('Você ganhou!')

#elif (numero + sorteado) %2 != 0 and aposta == 'ímpar':
    #print('Você ganhou!')

#else:
    #print('Você perdeu!')

#-------------------------------------------------------------------------------

#salario = float (input('Digite o valor do salário: '))

#desconto = salario - salario * 0.11

#descontoMax = salario - 318.20

#if desconto <= 318.20 and salario != 0:
     #print('O valor do salário total com o desconto ficou de',desconto)

#elif salario == 0:
     #print('Valor do salário inválido!')

#else:
    #print('O valor do salário total com o desconto ficou de',descontoMax)

#-----------------------------------------------------------------------------------

#valor = float (input('Digite o valor do produto: '))

#venda20 = valor + valor * 0.45

#venda50 = valor + valor * 0.35

#vendaMaior = valor + valor * 0.25

#if valor < 20:
    #print('Valor de venda: ',venda20)

#elif valor > 20 and valor <= 50:
    #print('Valor de venda: ',venda50)

#else:
    #print('valor da venda: ',vendaMaior)    

#-------------------------------------------------------------------------------------

cotacaoDolar = float (input('Digite a cotação do Real para Dólar: '))

cotacaoDolar_Real = float (input('Digite a cotação de Dólar para Real: '))

CotacaoDolar_Euro = float (input('Digite a cotação do Dólar para Euro: '))

cotacaoEuro_Dolar = float (input('Digite a cotação do Euro para Dólar: '))

cotacaoEuro_Real = float (input('Digite a cotaçõ de Euro para Real: '))

cotacaoEuro = float (input('Digite a cotação do Real para Euro: '))

resposta = input('Digite a opção desejada:\n1- Converter de Real para Euro\n2- Converter de real para Dólar\n3- Converter de Euo para Dólar\n4- Converter de Euro para Real\n5- Converter de Dólar para Euro\n6- Converter de Dólar para Real\n')

if resposta == '1':
    quantidade_real1 = float (input('Quantos reais você quer converter para Euro? '))

    Real_Euro = quantidade_real1 / cotacaoEuro

    print('\n',quantidade_real1,'equivale a',Real_Euro,'Euros')

elif resposta == '2':
    quantidade_real2 = float (input('Quantos reais você quer converter para Dólar? '))

    Real_Dolar = quantidade_real2 / cotacaoDolar

    print('\n',quantidade_real2,'equivale a',Real_Dolar,'dólares')

elif resposta == '3':
    quantidade_euro1 = float (input('Quantos Euros você quer converter para Dólar? '))

    Euro_Dolar = quantidade_euro1 / cotacaoEuro_Dolar

    print('\n',quantidade_euro1,'equivale a',Euro_Dolar,'dólares')

elif resposta == '4':
    quantidade_euro2 = float (input('Quantos Euros você quer converter para Real? '))

    Euro_Real = quantidade_euro2 / cotacaoEuro_Real

    print('\n',quantidade_euro2,'equivale a', Euro_Real,'reais')

elif resposta == '5':
    quantidade_dolar1 = float (input('Quantos dólares você quer converter para Euro? '))

    Dolar_Euro = quantidade_dolar1 / CotacaoDolar_Euro

    print('\n',quantidade_dolar1,'equivale a',Dolar_Euro,'Euros')

elif resposta == '6':
    quantidade_dolar2 = float (input('Quantos dólares você quer converter para Real? '))

    Dolar_Real = quantidade_dolar2 / cotacaoDolar_Real

    print('\n',quantidade_dolar2,'equivale a',Dolar_Real,'reais')

else:
    print('Resposta Inválida!')
