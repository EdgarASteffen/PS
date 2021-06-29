import json


# Abrir o arquivo JSON corrompido - codigo retirado de uma vídeoaula do YouTube
def ler_JSONcorrompido():
    with open('broken-database.json', 'r', encoding='utf8') as f:
        return json.load(f)


# Criar um novo JSON com os erros corrigidos - codigo retirado de uma vídeoaula do YouTube
def salvar_JSONcorrigido(dicionario):
    with open('saida.json', 'w', encoding='utf8') as f:
        return json.dump(dicionario, f, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ": "))


# Abrir o arquivo JSON corrigido para validação - codigo retirado de uma vídeoaula do YouTube
def ler_JSONcorrigido():
    with open('saida.json', 'r', encoding='utf8') as f:
        return json.load(f)


# Função para transformar str em float (PREÇOS)
def corrige_precos(dicionario):
    for x in range(10):
        dicionario[x]['price'] = float(dicionario[x]['price'])

    return dicionario[x]['price']


# Função para substituir as letras erradas (NOMES)
def corrige_nomes(dicionario):
    for x in range(10):
        dicionario[x]['name'] = (dicionario[x]['name'].replace("æ", "a"))
        dicionario[x]['name'] = (dicionario[x]['name'].replace("¢", "c"))
        dicionario[x]['name'] = (dicionario[x]['name'].replace("ø", "o"))
        dicionario[x]['name'] = (dicionario[x]['name'].replace("ß", "b"))

    return dicionario[x]['name']


# Função para adicionar o campo 'quantity' (QUANTIDADE)
def corrige_qtd(dicionario):
    for x in range(10):
        if 'quantity' in dicionario[x]:
            pass
        else:
            dicionario[x]["quantity"] = 0

    return dicionario[x]['quantity']


# Função para ordenaçao dos produtos primeiro por categoria
def ordena_produtosID(codigo):
    return codigo['id']


def ordena_produtosCAT(categoria):
    return categoria['category']


# Função para o valor total dos produtos por categoria - usando o arquivo saida.JSON
def total_produtos(valorProdutos):
    totalEletroDo = 0
    totalEletrico = 0
    totalPanelas = 0
    totalAcessorios = 0
    totalEstoque = 0

    for x in range(10):
        if valorProdutos[x]['category'] == "Eletrodomésticos":
            totalEletroDo = totalEletroDo + \
                (valorProdutos[x]['quantity'] * valorProdutos[x]['price'])

        if valorProdutos[x]['category'] == "Eletrônicos":
            totalEletrico = totalEletrico + \
                (valorProdutos[x]['quantity'] * valorProdutos[x]['price'])

        if valorProdutos[x]['category'] == "Panelas":
            totalPanelas = totalPanelas + \
                (valorProdutos[x]['quantity'] * valorProdutos[x]['price'])

        if valorProdutos[x]['category'] == "Acessórios":
            totalAcessorios = totalAcessorios + \
                (valorProdutos[x]['quantity'] * valorProdutos[x]['price'])

    totalEstoque = totalAcessorios + totalEletrico + totalEletroDo + totalPanelas

    print("Valor total de ACESSÓRIOS - R$ {:.2f}".format(totalAcessorios))
    print("Valor total de ELETRODOMÉSTICOS - R$ {:.2f}".format(totalEletroDo))
    print("Valor total de ELETRÔNICOS - R$ {:.2f}".format(totalEletrico))
    print("Valor total de PANELAS - R$ {:.2f}".format(totalPanelas))

    print("\nValor total de ESTOQUE - R$ {:.2f}".format(totalEstoque))


# 1. Recuperação dos dados originais do banco de dados
# A. Ler o arquivo Json do banco de dados corrompido
dicionarioJSON = ler_JSONcorrompido()

# B. Corrigir nomes
corrige_nomes(dicionarioJSON)

# C. Corrigir preços
corrige_precos(dicionarioJSON)

# D. Corrigir quantidades
corrige_qtd(dicionarioJSON)

# E. Exportar um arquivo JSON com o banco corrigido
salvar_JSONcorrigido(dicionarioJSON)


# 2. Validação do banco de dados corrigido
# Input o banco de dados corrigido da questão 1
validarCorrecao = ler_JSONcorrigido()

# A. Função que imprime a lista de nomos de produtos, ordenados por categoria
validarCorrecao.sort(key=ordena_produtosID)
validarCorrecao.sort(key=ordena_produtosCAT)

print("\n------ PRODUTOS NO ESTOQUE ------\n")
for x in range(10):
    print(validarCorrecao[x]['category'], " - ",
          validarCorrecao[x]['id'], " ", validarCorrecao[x]['name'])

# # B. Uma função que calcula qual é o valor total do estoque por categoria
print("\n------ VALOR DO ESTOQUE ------\n")
total_produtos(validarCorrecao)


print(type(validarCorrecao))
