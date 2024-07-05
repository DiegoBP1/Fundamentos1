def cumprimentar(nome):
    print(f"Olá, {nome}!")


nome = input("Digite o nome da pessoa: ")
cumprimentar(nome)

#----------------------------------------------

def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


num = int(input("Digite um número inteiro para ver a tabuada: "))
tabuada(num)

#-------------------------------------------------

def mediaUnisinos(nota_grau_a, nota_grau_b):
    media_final = (nota_grau_a + nota_grau_b) / 2
    return media_final


nota_a = float(input("Digite a nota do Grau A: "))
nota_b = float(input("Digite a nota do Grau B: "))

resultado_final = mediaUnisinos(nota_a, nota_b)
print(f"O resultado do grau final é: {resultado_final}")

#---------------------------------------------


import random

def sorteio(inicio, fim):
    numero_sorteado = random.randint(inicio, fim)
    return numero_sorteado


inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))

numero_sorteado = sorteio(inicio, fim)
print(f"Número sorteado dentro do intervalo [{inicio}, {fim}]: {numero_sorteado}")

#---------------------------------------------


def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("Erro: Divisão por zero!")
        return None


def main():
    print("Escolha a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    opcao = int(input("Digite o número da operação desejada (1/2/3/4): "))
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = somar(num1, num2)
        print(f"Resultado da soma: {resultado}")
    elif opcao == 2:
        resultado = subtrair(num1, num2)
        print(f"Resultado da subtração: {resultado}")
    elif opcao == 3:
        resultado = multiplicar(num1, num2)
        print(f"Resultado da multiplicação: {resultado}")
    elif opcao == 4:
        resultado = dividir(num1, num2)
        if resultado is not None:
            print(f"Resultado da divisão: {resultado}")
    else:
        print("Opção inválida. Por favor, escolha uma operação válida (1/2/3/4).")

if __name__ == "__main__":
    main()


#-----------------------------------------------------------

import random


itens_comuns = 0
itens_raros = 0
itens_lendarios = 0


def abrir_caixa():
    global itens_comuns, itens_raros, itens_lendarios
    
    
    sorteio = random.random()  
    
    if sorteio <= 0.80:
      
        itens_comuns += 1
        print("Você obteve um item comum!")
    elif sorteio <= 0.99:
        # Item raro
        itens_raros += 1
        print("Você obteve um item raro!")
    else:
     
        itens_lendarios += 1
        print("Você obteve um item lendário!")


def consultar_itens():
    print(f"Itens coletados:")
    print(f"Comuns: {itens_comuns}")
    print(f"Raros: {itens_raros}")
    print(f"Lendários: {itens_lendarios}")


def main():
    while True:
        print("\n===== Sistema de Lootbox =====")
        print("1 - Abrir uma caixa")
        print("2 - Consultar itens coletados")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            abrir_caixa()
        elif opcao == '2':
            consultar_itens()
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()