num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num2!= 0:
    resultado = num1 / num2
    print(f"O resultado da divisão é:",resultado)
else:
    print("Erro: Não é possível dividir por zero!")

#------------------------------------------------------------------

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if A + B < A + C:
    print("A soma de A + B é menor que A + C")
else:
    print("A soma de A + B não é menor que A + C")

#---------------------------------------------------------------------

num = float(input("Digite um número: "))

if num > 0:
    resultado = num * 2
    print(f"O dobro de num é",resultado)
else:
    resultado = num * 3
    print(f"O triplo de", num, "é",resultado)

#------------------------------------------------------------------------

num = int(input("Digite um número inteiro: "))

if num % 3 == 0:
    print("O número é divisível por 3")
else:
    print("O número não é divisível por 3")

    #-------------------------------------------------------------------


    num = int(input("Digite um número: "))

if num % 2 == 0:
    print("O número é par")
else:
    print(f"O número é ímpar")

#----------------------------------------------------

import random

print("Bem-vindo ao jogo de PAR ou ÍMPAR!")

aposta = input("Você aposta em PAR ou ÍMPAR? (P/I): ")

while aposta.upper() not in ["P", "I"]:
    aposta = input("Você aposta em PAR ou ÍMPAR? (P/I): ")

num_usuario = int(input("Digite um número de 0 a 5: "))

while num_usuario < 0 or num_usuario > 5:
    num_usuario = int(input("Digite um número de 0 a 5: "))

num_sorteado = random.randint(0, 5)

soma = num_usuario + num_sorteado

print(f"Você escolheu {aposta.upper()} e digitou {num_usuario}. O número sorteado foi {num_sorteado}. A soma é {soma}.")

if (aposta.upper() == "P" and soma % 2 == 0) or (aposta.upper() == "I" and soma % 2 != 0):
    print("Você venceu!")
else:
    print("O programa venceu!") 


#-------------------------------------------------------------------------------

def calcular_desconto(salario):
    desconto_maximo = 318.20
    desconto_calculado = salario * 0.11

    if desconto_calculado > desconto_maximo:
        return desconto_maximo
    else:
        return desconto_calculado

salario = float(input("Digite o salário do funcionário: "))

desconto = calcular_desconto(salario)

print("O desconto previdenciário é de R$",desconto)


#-----------------------------------------------------------------------------

def calcular_valor_venda(valor_compra):
    if valor_compra < 20:
        lucro = 0.45
    elif valor_compra <= 50:
        lucro = 0.35
    else:
        lucro = 0.25

    valor_venda = valor_compra * (1 + lucro)

    return valor_venda

valor_compra = float(input("Digite o valor do produto: "))

valor_venda = calcular_valor_venda(valor_compra)

print(f"O valor de venda é de R$",valor_venda)

#------------------------------------------------------------------------------

def converter_moedas():
    cotacao_euro = float(input("Digite a cotação do Euro em relação ao Real: "))
    cotacao_dolar = float(input("Digite a cotação do Dólar em relação ao Real: "))

    while True:
        print("Conversor de Moedas")
        print("1) Converter de Real para Euro")
        print("2) Converter de Real para Dólar")
        print("3) Converter de Euro para Dólar")
        print("4) Converter de Euro para Real")
        print("5) Converter de Dólar para Euro")
        print("6) Converter de Dólar para Real")
        print("7) Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 7:
            break

        valor_origem = float(input("Digite o valor a ser convertido: "))

        if opcao == 1:
            valor_destino = valor_origem / cotacao_euro
            print(valor_origem, "Reais é igual a",valor_destino,"Euros")
        elif opcao == 2:
            valor_destino = valor_origem / cotacao_dolar
            print(valor_origem,"Reais é igual a",valor_destino,"Dólares")
        elif opcao == 3:
            valor_destino = cotacao_dolar / cotacao_euro * valor_origem
            print(valor_origem,"Euros é igual a",valor_destino,"Dólares")
        elif opcao == 4:
            valor_destino = valor_origem * cotacao_euro
            print(valor_origem,"Euros é igual a",valor_destino,"Reais")
        elif opcao == 5:
            valor_destino = cotacao_euro / cotacao_dolar * valor_origem
            print(valor_origem,"Dólares é igual a",valor_destino,"Euros")
        elif opcao == 6:
            valor_destino = valor_origem * cotacao_dolar
            print(valor_origem,"Dólares é igual a",valor_destino,"Reais")

converter_moedas()

#-----------------------------------------------------------------------------


import random

def lancar_dado(num_faces):
    return random.randint(1, num_faces)

def main():
    num_faces = int(input("Digite o número de faces do dado (4, 6, 8, 10, 12 ou 16): "))

    if num_faces not in [4, 6, 8, 10, 12, 16]:
        print("Número de faces inválido. Tente novamente!")
        return

    resultado = lancar_dado(num_faces)

    print("Você lançou o dado e obteve",resultado,"!")

#---------------------------------------------------------------------------


def calcular_notas(valor):
    notas = [100, 50, 20, 10, 5, 1]
    quantidade_notas = [0, 0, 0, 0, 0, 0]

    for i, nota in enumerate(notas):
        quantidade_notas[i] = valor // nota
        valor %= nota

    return quantidade_notas

def imprimir_notas(quantidade_notas):
    notas = [100, 50, 20, 10, 5, 1]
    nomes_notas = ["R$ 100", "R$ 50", "R$ 20", "R$ 10", "R$ 5", "R$ 1"]

    for i, quantidade in enumerate(quantidade_notas):
        if quantidade > 0:
            print(quantidade,"nota(s) de {nomes_notas[i]}")

def main():
    valor = int(input("Digite o valor a ser entregue: "))
    quantidade_notas = calcular_notas(valor)
    imprimir_notas(quantidade_notas)

    #---------------------------------------------------------

    
idade = int(input("Digite a idade do nadador: "))


if idade >= 5 and idade <= 7:
    categoria = "Infantil A"
elif idade >= 8 and idade <= 10:
    categoria = "Infantil B"
elif idade >= 11 and idade <= 13:
    categoria = "Juvenil A"
elif idade >= 14 and idade <= 17:
    categoria = "Juvenil B"
else:
    categoria = "Sênior"


print("O nadador com",idade,"anos está na categoria",categoria)

#-------------------------------------------------------------------


def calcular_media(a, b):
    return (a + b) / 2


def verificar_aprovacao(media):
    if media >= 6:
        return "aprovado"
    elif media >= 4:
        return "recuperação"
    else:
        return "reprovado"


def main():
    
    nota_a = float(input("Digite a nota do Grau A: "))
    nota_b = float(input("Digite a nota do Grau B: "))
   
    media_inicial = calcular_media(nota_a, nota_b)
    
    
    situacao = verificar_aprovacao(media_inicial)
    
    if situacao == "aprovado":
        print(f"O aluno está aprovado com média final {media_inicial:.2f}.")
    elif situacao == "recuperação":
        print(f"O aluno ficou em recuperação com média final {media_inicial:.2f}.")
        
        
        substituir = input("Deseja substituir a nota do Grau A ou do Grau B? (Digite 'a' ou 'b'): ").lower()
        
        if substituir == 'a':
            nota_c = float(input("Digite a nota do Grau C (substituindo a nota do Grau A): "))
            media_substituida = calcular_media(nota_c, nota_b)
        elif substituir == 'b':
            nota_c = float(input("Digite a nota do Grau C (substituindo a nota do Grau B): "))
            media_substituida = calcular_media(nota_a, nota_c)
        else:
            print("Opção inválida. Programa encerrado.")
            return
        
      
        nova_situacao = verificar_aprovacao(media_substituida)
        
        if nova_situacao == "aprovado":
            print(f"Após a substituição, o aluno está aprovado com média final {media_substituida:.2f}.")
        else:
            print(f"Após a substituição, o aluno está reprovado com média final {media_substituida:.2f}.")

    else:
        print(f"O aluno está reprovado com média final {media_inicial:.2f}.")


main()

#------------------------------------------------------------------


def calcular_valor_plano(idade_conveniado, idades_dependentes):
    valor_base = 300
    adicional_crianca = 100
    adicional_jovem = 220
    adicional_adulto = 395
    adicional_idoso = 480

    valor_total = valor_base

    for idade in idades_dependentes:
        if idade < 10:
            valor_total += adicional_crianca
        elif 10 <= idade <= 30:
            valor_total += adicional_jovem
        elif 31 <= idade <= 60:
            valor_total += adicional_adulto
        elif idade > 60:
            valor_total += adicional_idoso

    return valor_total

idade_conveniado = int(input("Digite a idade do conveniado: "))
num_dependentes = int(input("Digite o número de dependentes: "))
idades_dependentes = []

for i in range(num_dependentes):
    idade = int(input(f"Digite a idade do dependente {i+1}: "))
    idades_dependentes.append(idade)

valor_total = calcular_valor_plano(idade_conveniado, idades_dependentes)
print(f"O valor total a ser pago pelo plano de saúde é: R$ {valor_total}")

#-----------------------------------------------------------------------------

def calcular_valor_final(preco_etiqueta, condicao_pagamento):
    if condicao_pagamento == 1:
        valor_final = preco_etiqueta * 0.85
    elif condicao_pagamento == 2:
        valor_final = preco_etiqueta * 0.90
    elif condicao_pagamento == 3:
        valor_final = preco_etiqueta
    elif condicao_pagamento == 4:
        valor_final = preco_etiqueta * 1.10
    else:
        raise ValueError("Condição de pagamento inválida!")
    return valor_final

# Exemplo de uso do programa
preco_etiqueta = float(input("Digite o preço de etiqueta do produto: "))
print("Escolha a condição de pagamento:")
print("1 - À vista em dinheiro, recebe 15% de desconto")
print("2 - À vista no cartão de crédito, recebe 10% de desconto")
print("3 - Em duas vezes, preço normal de etiqueta sem juros")
print("4 - Em três vezes, preço normal de etiqueta mais juros de 10%")

condicao_pagamento = int(input("Digite o código da condição de pagamento escolhida: "))

try:
    valor_final = calcular_valor_final(preco_etiqueta, condicao_pagamento)
    print(f"O valor final a ser pago é: R$ {valor_final:.2f}")
except ValueError as e:
    print(e)