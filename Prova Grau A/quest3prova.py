PoInicio = 100 
EssenciaInicio = 50
Raizinicio = 45
OrvalhoIncio = 30
FloresInicio = 200
ElixirInicio = 20
LagrimasInicio = 15


def pocoes():
    print('O que deseja fazer?')
    print('1 - Fazer poção')
    print('2- Consultar Ingredientes')
    print('3 - SAIR')
    item = input('Escolha uma opção: ')
    return item

def fazerpocao():
    qual = print(input('Qual poção deseja fazer? '))
    if qual == '1':
        Poagora = PoInicio - 30
        EssenciaAgora = EssenciaInicio - 20
        FloresAgora = FloresInicio - 20
        LagrimasAgora = LagrimasInicio - 10
    elif qual == '2':
        OravlhoAgora = OrvalhoIncio - 10
        RaizAgora = Raizinicio - 30
        FloresAgora = FloresInicio - 30
    elif qual == '3':
        EssenciaAgora = EssenciaInicio - 30
        PoAgora = PoInicio - 50
    elif qual == '4':
        OrvalhoAgora = OrvalhoIncio - 10
        FloresAgora = FloresInicio - 50
        LagrimasAgora = LagrimasInicio - 5
    elif qual == 5:
        ElixirAgora = ElixirInicio - 10
        RaizAgora = Raizinicio - 15                

def ingred():
    print('Pó de fênix:',PoInicio,'g')
    print('Essência Celestial:',EssenciaInicio,'ml')
    print('Raiz de Dragão:',Raizinicio,'ml')
    print('Orvalho Lunar:',OrvalhoIncio,'ml')
    print('Flores Secas:',FloresInicio,'g')
    print('Elixir Amargo:',ElixirInicio,'ml')
    print('Lágrimas de Unicórnio:',LagrimasInicio,'ml')
    print(ingred())

def sair():
    print('Saindo...')    


escolha = '' 

while(escolha != 3):
    escolha = pocoes()
    if escolha == '1':
        fazerpocao()
    elif escolha == '2':
        ingred()
    elif escolha == '3':
        sair()
    else:
        print('Opção desconhecida!')            
        