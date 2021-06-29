import json


def ler_JSON():
    with open('bderro.json', 'r', encoding='utf8') as f:
        return json.load(f)


def corrige_precos(thisdict):  # Função para transformar str em float (PREÇOS)
    for x in range(10):
        thisdict[x]['price'] = float(thisdict[x]['price'])

    return thisdict[x]['price']


def corrige_nomes(thisdict):  # Função para substituir as letras erradas (NOMES)
    for x in range(10):
        thisdict[x]['name'] = (thisdict[x]['name'].replace("æ", "a"))
        thisdict[x]['name'] = (thisdict[x]['name'].replace("¢", "c"))
        thisdict[x]['name'] = (thisdict[x]['name'].replace("ø", "o"))
        thisdict[x]['name'] = (thisdict[x]['name'].replace("ß", "b"))

    return thisdict[x]['name']


def corrige_qtd(thisdict):  # Função para adicionar o campo 'quantity' (QUANTIDADE)
    for x in range(10):
        if 'quantity' in thisdict[x]:
            pass
        else:
            thisdict[x]["quantity"] = 0

    return thisdict[x]['quantity']


def total_produtos(thisdict):  # Função para o valor total dos produtos por categoria
    totalEletroDo = 0
    totalEletrico = 0
    totalPanelas = 0
    totalAcessorios = 0

    for x in range(10):
        if thisdict[x]['category'] == "Eletrodomésticos":
            totalEletroDo = totalEletroDo + \
                (thisdict[x]['quantity'] * thisdict[x]['price'])

        if thisdict[x]['category'] == "Eletrônicos":
            totalEletrico = totalEletrico + \
                (thisdict[x]['quantity'] * thisdict[x]['price'])

        if thisdict[x]['category'] == "Panelas":
            totalPanelas = totalPanelas + \
                (thisdict[x]['quantity'] * thisdict[x]['price'])

        if thisdict[x]['category'] == "Acessórios":
            totalAcessorios = totalAcessorios + \
                (thisdict[x]['quantity'] * thisdict[x]['price'])

    print(totalPanelas)
    print(totalEletroDo)
    print(totalEletrico)
    print(totalAcessorios)


def salvarJSON(thisdict):  # Preciso arrumar isso aqui!!
    with open('databaseCorreto.json', 'w', encoding='utf8') as f:
        return json.dump(thisdict, f)


# thisdict = [
#     {
#         "id": 5677240,
#         "name": "Cønjuntø de Pænelæs æntiæderentes ¢øm 05 Peçæs Pæris",
#         "quantity": 21,
#         "price": "192.84",
#         "category": "Panelas"
#     },
#     {
#         "id": 9628920,
#         "name": "Lævæ & Se¢æ 10,2 Kg Sæmsung E¢ø ßußßle ßræn¢æ ¢øm 09 Prøgræmæs de Lævægem",
#         "quantity": 57,
#         "price": 3719.70,
#         "category": "Eletrodomésticos"
#     },
#     {
#         "id": 1316334,
#         "name": "Refrigerædør ßøttøm Freezer Ele¢trølux de 02 Pørtæs Frøst Free ¢øm 598 Litrøs",
#         "quantity": 12,
#         "price": 3880.23,
#         "category": "Eletrodomésticos"
#     },
#     {
#         "id": 6502394,
#         "name": "Føgãø de Pisø Ele¢trølux de 04 ßø¢æs, Mesæ de Vidrø Prætæ",
#         "quantity": 37,
#         "price": "1419",
#         "category": "Eletrodomésticos"
#     },
#     {
#         "id": 9576720,
#         "name": "Førnø Mi¢rø-øndæs Pænæsøni¢ ¢øm ¢æpæ¢idæde de 21 Litrøs ßræn¢ø",
#         "quantity": 13,
#         "price": "358.77",
#         "category": "Eletrodomésticos"
#     },
#     {
#         "id": 8875900,
#         "name": "Smært TV 4K Søny LED 65” 4K X-Reælity Prø, UpS¢ælling, Møtiønfløw XR 240 e Wi-F",
#         "quantity": 0,
#         "price": 5799.42,
#         "category": "Eletrônicos"
#     },
#     {
#         "id": 9746439,
#         "name": "Høme Theæter LG ¢øm ßlu-ræy 3D, 5.1 ¢ænæis e 1000W",
#         "quantity": 80,
#         "price": 2199,
#         "category": "Eletrônicos"
#     },
#     {
#         "id": 2162952,
#         "name": "Kit Gæmer æ¢er - Nøteßøøk + Heædset + Møuse",
#         "price": "25599.00",
#         "category": "Eletrônicos"
#     },
#     {
#         "id": 3500957,
#         "name": "Mønitør 29 LG FHD Ultræwide ¢øm 1000:1 de ¢øntræste",
#         "quantity": 18,
#         "price": 1559.40,
#         "category": "Eletrônicos"
#     },
#     {
#         "id": 1911864,
#         "name": "Møuse Gæmer Predætør ¢estus 510 Føx Pretø",
#         "price": "699",
#         "category": "Acessórios"
#     }]


thisdict = ler_JSON()
corrige_precos(thisdict)
corrige_nomes(thisdict)
corrige_qtd(thisdict)
# total_produtos(thisdict)

# salvarJSON(thisdict)

print(type(thisdict))

# for x in range(10):
#     print(thisdict[x]['name'])
# print(json.dumps(thisdict, indent=4))
