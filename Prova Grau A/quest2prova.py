def divisivelporN(num1,num2):
    if num1 %num2 == 0:
        return True
    else:
        return False
    


num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))

if num2 == 0:
    print('Não é possível dividir um número por 0!')


print(divisivelporN(num1,num2))