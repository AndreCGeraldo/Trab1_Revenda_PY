from asyncio.proactor_events import _ProactorDuplexPipeTransport
import os.path
from tracemalloc import start

carros = []
marcas = []
precos = []
anos = []


def titulo(mensa, simbolo="=-"):
    print()
    print(mensa)
    print(simbolo*40)


def incluir():
    titulo("Inclusão de Carros")
    carro = input("Modelo do Carro: ")
    marca = input("Marca do Veículo: ")
    ano = input("Ano do Veículo: ")
    preco = float(input("Preço R$: "))
    carros.append(carro)
    marcas.append(marca)
    anos.append(ano)
    precos.append(preco)
    print()
    print("Ok! Veículo cadastrado com Sucesso")


def listar():
    titulo("Listagem dos Veículos")
    print("\nNº Carro.................. Marca.............. Ano......... Preço R$:")
    print("="*69)
    for i, (carro, marca, ano, preco) in enumerate(zip(carros, marcas, anos, precos,), start=1):
        print(f"{i:2d} {carro:23s} {marca:19s} {ano} {preco:17.2f}")
    print("="*69)


def alterar():
    listar()
    titulo("Alteração de Veículo")
    alt = int(input("Nº do Veículo (0, para sair): "))
    if alt == 0:
        return
    if alt > len(carros) or alt < 0:
        print("Erro... número inválido")
        return
    novo_preco = float(input(f"Novo preço do Veículo '{carros[alt-1]}' R$: "))
    precos[alt-1] = novo_preco
    print("Ok! Preço alterado com sucesso.")


def excluir():
    listar()
    titulo("Exclusão de Veículo")
    exc = int(input("Nº do Veículo (0, para sair): "))
    if exc == 0:
        return
    if exc > len(carros) or exc < 0:
        print("Erro... número inválido")
        return

    carros.pop(exc-1)
    precos.pop(exc-1)
    print("Ok! Veículo removido com Sucesso")



def pesquisar():
    titulo("Pesquisa de Veículos")
    palavra = input("Qual Carro: ")
    print("\nCarro..................| Marca...... Ano.... Preço R$:")
    print("="*54)
    contador = 0
    for carro, marca, ano, preco in zip(carros, marcas, anos, precos):
        if palavra.upper() in carro.upper():
            print(f"{carro:23s}| {marca:11s} {ano} {preco:12.2f}")
            contador += 1
    if contador == 0:
        print(f"* Obs.: Não há Veículo com a palavra - '{palavra}'")
    print("="*54)


def pesquisarMarca():
    titulo("Pesquisa de Veículos")
    palavra = input("Qual Marca: ")
    print("\nMarca......| Carro.................. Ano.... Preço R$:")
    print("="*54)
    contador = 0
    for carro, marca, ano, preco in zip(carros, marcas, anos, precos):
        if palavra.upper() in marca.upper():
            print(f"{marca:11s}| {carro:23s} {ano} {preco:12.2f}")
            contador += 1
    if contador == 0:
        print(f"* Obs.: Não há Veículo da Marca '{palavra}' encontrado.")
    print("="*54)


def resumo():
    titulo("Resumo com Totais do Cadastro da Revanda")
    num = len(carros)
    soma = sum(precos)
    maximo = max(precos)
    minimo = min(precos)
    media = soma / num
    print(f"Nº de veículos Cadastrados: {num}")
    print(f"Maior preço do Estoque R$.......:{maximo:12.2f}")
    print(f"Menor preço do Estoque R$.......:{minimo:12.2f}")
    print(f"Preço Médio dos veículos........:{media:12.2f}")
    print(f"Total em Estoque R$.............:{soma:12.2f}")





def salvar():
    with open("carros.txt", "w") as arq:
        for carro, marca, ano, preco in zip(carros, marcas, anos, precos):
            arq.write(f"{carro};{marca};{ano};{preco}\n")


def carregar_dados():
    with open("carros.txt", "r") as arq:
        linhas = arq.read().splitlines()
    for linha in linhas:
        partes = linha.split(";")
        carros.append(partes[0])
        marcas.append(partes[1])
        anos.append(partes[2])
        precos.append(float(partes[3]))


if os.path.exists("carros.txt"):
    carregar_dados()



while True:
    titulo("Cadastro de Veículos", "=")
    print("1. Cadastrar Carros")
    print("2. Listagem de Carros")
    print("3. Alterar Preço")
    print("4. Excluir")
    print("5. Pesquisar p/ Carro")
    print("6. Pesquisar p/ Marca")
    print("7. Resumo")
    print("8. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        alterar()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        pesquisar()
    elif opcao == 6:
        pesquisarMarca()
    elif opcao == 7:
        resumo()
    else:
        break


salvar()
