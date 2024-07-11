import csv
from datetime import datetime

# Função para carregar dados do CSV
def carregar_dados(nome_arquivo):
    with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

# Função para salvar dados no CSV
def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = dados[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dados)

# Função para cadastrar um novo felino
def cadastrar_felino(dados):
    felino = {
        "Nome": input("Nome: "),
        "Sexo": input("Sexo: "),
        "Idade": input("Idade: "),
        "Raça": input("Raça: "),
        "Cor Predominante": input("Cor Predominante: "),
        "Castrado": input("Castrado (Sim/Não): "),
        "FIV+": input("FIV+ (Sim/Não): "),
        "FELV+": input("FELV+ (Sim/Não): "),
        "Data de Resgate": input("Data de Resgate (dd/mm/aaaa): "),
        "Adotado": input("Adotado (Sim/Não): "),
        "Lar Temporário": input("Lar Temporário (Sim/Não): "),
        "Data de Adoção/Hospedagem": input("Data de Adoção/Hospedagem (dd/mm/aaaa): "),
        "Tutor": input("Tutor: "),
        "Contato": input("Contato: "),
        "Data da Última Vacina": input("Data da Última Vacina (dd/mm/aaaa): "),
        "Data da Última Desverminação": input("Data da Última Desverminação (dd/mm/aaaa): "),
        "Data do Último Antipulgas": input("Data do Último Antipulgas (dd/mm/aaaa): "),
        "Informações Extras": input("Informações Extras: ")
    }
    dados.append(felino)


def alterar_status_felino(dados):
    listar_felinos(dados)
    index = int(input("Escolha o número do felino que deseja alterar: ")) - 1
    felino = dados[index]
    print("Informações atuais do felino:")
    for i, (key, value) in enumerate(felino.items()):
        print(f"{i + 1}. {key}: {value}")
    while True:
        escolha = input("Digite o número da informação que deseja alterar (ou '0' para voltar): ")
        if escolha == '0':
            break
        key = list(felino.keys())[int(escolha) - 1]
        felino[key] = input(f"Novo valor para {key}: ")


def consultar_felino(dados):
    listar_felinos(dados)
    index = int(input("Escolha o número do felino que deseja consultar: ")) - 1
    felino = dados[index]
    for key, value in felino.items():
        print(f"{key}: {value}")


def apresentar_estatisticas(dados):
    total = len(dados)
    machos = sum(1 for felino in dados if felino["Sexo"].lower() == "m")
    femeas = total - machos
    adotados = sum(1 for felino in dados if felino["Adotado"].lower() == "sim")
    nao_adotados = total - adotados
    fiv_negativo = sum(1 for felino in dados if felino["FIV+"].lower() == "não" and felino["FELV+"].lower() == "não")
    fiv_positivo = sum(1 for felino in dados if felino["FIV+"].lower() == "sim")
    felv_positivo = sum(1 for felino in dados if felino["FELV+"].lower() == "sim")
    ambos_positivo = sum(1 for felino in dados if felino["FIV+"].lower() == "sim" and felino["FELV+"].lower() == "sim")

    print(f"Porcentagem de machos: {machos / total * 100:.2f}%")
    print(f"Porcentagem de fêmeas: {femeas / total * 100:.2f}%")
    print(f"Porcentagem de adotados: {adotados / total * 100:.2f}%")
    print(f"Porcentagem de não adotados: {nao_adotados / total * 100:.2f}%")
    print(f"Porcentagem de felinos negativos para FIV e FELV: {fiv_negativo / total * 100:.2f}%")
    print(f"Porcentagem de felinos positivos para FIV: {fiv_positivo / total * 100:.2f}%")
    print(f"Porcentagem de felinos positivos para FELV: {felv_positivo / total * 100:.2f}%")
    print(f"Porcentagem de felinos positivos para ambos FIV e FELV: {ambos_positivo / total * 100:.2f}%")


def listar_felinos(dados):
    for i, felino in enumerate(dados, 1):
        print(f"{i}. {felino['Nome']}")


def filtrar_dados(dados):
    escolha = input("1. Consultar gatos resgatados por período\n2. Consultar gatos adotados por período\nEscolha uma opção: ")
    ano_inicio = int(input("Ano de início: "))
    ano_fim = int(input("Ano de fim: "))
    
    if escolha == '1':
        filtrados = [felino for felino in dados if ano_inicio <= int(felino["Data de Resgate"].split('/')[-1]) <= ano_fim]
    elif escolha == '2':
        filtrados = [felino for felino in dados if ano_inicio <= int(felino["Data de Adoção/Hospedagem"].split('/')[-1]) <= ano_fim]

    for felino in filtrados:
        print(f"{felino['Nome']} - Resgatado em: {felino['Data de Resgate']} - Adotado em: {felino['Data de Adoção/Hospedagem']}")


def main():
    nome_arquivo = 'gatinhos.csv' 
    dados = carregar_dados(nome_arquivo)
    
    while True:
        print("\nMenu Principal")
        print("1. Cadastrar felino")
        print("2. Alterar status de felino")
        print("3. Consultar informações sobre felino")
        print("4. Apresentar estatísticas gerais")
        print("5. Filtragem de dados")
        print("6. Salvar")
        print("7. Sair do programa")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_felino(dados)
        elif opcao == '2':
            alterar_status_felino(dados)
        elif opcao == '3':
            consultar_felino(dados)
        elif opcao == '4':
            apresentar_estatisticas(dados)
        elif opcao == '5':
            filtrar_dados(dados)
        elif opcao == '6':
            salvar_dados(nome_arquivo, dados)
        elif opcao == '7':
            salvar_dados(nome_arquivo, dados)
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()