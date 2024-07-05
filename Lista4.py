import random

print("a. Números inteiros de 0 a 100:")
for i in range(101):
    print(i, end=" ")
print("\n")

print("b. Números pares de 20 a 50:")
for i in range(20, 51):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")

print("c. Números inteiros de 25 a 70 em ordem decrescente:")
for i in range(70, 24, -1):
    print(i, end=" ")
print("\n")

print("d. Números ímpares de 25 a 95 em ordem decrescente:")
for i in range(95, 24, -1):
    if i % 2 != 0:
        print(i, end=" ")
print("\n")

print("e. Soma e média de 15 números:")
soma = 0
for i in range(15):
    num = float(input(f"Digite o número {i+1}: "))
    soma += num
media = soma / 15
print(f"Soma: {soma}, Média: {media}\n")

print("f. Quantidade de números pares e ímpares:")
pares = 0
impares = 0
for i in range(10):
    num = int(input(f"Digite o número {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Pares: {pares}, Ímpares: {impares}\n")

print("g. Sorteio de 20 números entre -10 e 10:")
positivos = 0
negativos = 0
for _ in range(20):
    num = random.randint(-10, 10)
    if num > 0:
        print(f"{num} POSITIVO")
        positivos += 1
    elif num < 0:
        print(f"{num} NEGATIVO")
        negativos += 1
    else:
        print(f"{num} NULO")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}\n")

print("h. Soma de n números:")
n = int(input("Digite a quantidade de números a serem lidos: "))
soma = 0
for i in range(n):
    num = float(input(f"Digite o número {i+1}: "))
    soma += num
print(f"Soma dos números lidos: {soma}")


#-------------------------------------------------------------------------

import random

numero_sorteado = random.randint(1, 10)
tentativas = 3

print("Tente adivinhar o número sorteado entre 1 e 10. Você tem 3 tentativas.")

for tentativa in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite: "))

    if palpite == numero_sorteado:
        print("Parabéns! Você acertou o número.")
        break
    elif palpite < numero_sorteado:
        print("O número sorteado é maior que o seu palpite.")
    else:
        print("O número sorteado é menor que o seu palpite.")
    
    if tentativa == tentativas:
        print(f"Suas tentativas acabaram. O número sorteado era {numero_sorteado}.")


        #------------------------------------------------------------------------------


def mostrar_tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Entre com um número de 1 a 9: "))

if 1 <= numero <= 9:
    mostrar_tabuada(numero)
else:
    print("Número inválido. Por favor, entre com um número de 1 a 9.")


#------------------------------------------------------------------------------------


def encontrar_divisiveis(divisor, inicio_intervalo, fim_intervalo):
    for num in range(inicio_intervalo, fim_intervalo + 1):
        if num % divisor == 0:
            print(num)

divisor = int(input("Entre com o divisor: "))
inicio_intervalo = int(input("Entre com o valor inicial do intervalo: "))
fim_intervalo = int(input("Entre com o valor final do intervalo: "))

if inicio_intervalo <= fim_intervalo:
    print(f"Números divisíveis por {divisor} no intervalo de {inicio_intervalo} a {fim_intervalo}:")
    encontrar_divisiveis(divisor, inicio_intervalo, fim_intervalo)
else:
    print("Intervalo inválido. O valor inicial deve ser menor ou igual ao valor final.")