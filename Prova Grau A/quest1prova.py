def divisivelpor2(numero):
    print('Esse número é divisível por 2:',numero)
    if numero %2 == 0:
        return True
    else:
        return False

numero = int(input('Digite um número: '))
    
print(divisivelpor2(numero))
