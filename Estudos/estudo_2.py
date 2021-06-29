# Entrada manual dos dados do "broken-database.json" já que não consegui importar
# Arrumar a importação do arquivo "resolution.py"

# import json


# def lerJson():
#     with open('bderro.json', 'r', encoding='utf8') as f:
#         return json.load(f)


# thisdict = lerJson()

thisdict = [
    {
        "id": 5677240,
        "name": "Cønjuntø de Pænelæs æntiæderentes ¢øm 05 Peçæs Pæris",
        "price": "192.84",
        "category": "Panelas"
    },
    {
        "id": 9628920,
        "name": "Lævæ & Se¢æ 10,2 Kg Sæmsung E¢ø ßußßle ßræn¢æ ¢øm 09 Prøgræmæs de Lævægem",
        "quantity": 57,
        "price": 3719.70,
        "category": "Eletrodomésticos"
    },
    {
        "id": 6502394,
        "name": "Føgãø de Pisø Ele¢trølux de 04 ßø¢æs, Mesæ de Vidrø Prætæ",
        "quantity": 37,
        "price": "1419",
        "category": "Eletrodomésticos"
    },
    {
        "id": 2162952,
        "name": "Kit Gæmer æ¢er - Nøteßøøk + Heædset + Møuse",
        "price": "25599.00",
        "category": "Eletrônicos"
    }]

totalE = 0

# print(thisdict)
# print(type(thisdict['price']))

# for x in range(3):
#     print(thisdict[x]['name'])

# Função para transformar str em float (PREÇOS)
for x in range(4):
    thisdict[x]['price'] = float(thisdict[x]['price'])
######################################################################################

# for x in range(3):
#     print(thisdict[x]['price'])

# print(type(thisdict['price']))

# Função para substituir as letras erradas (NOMES)
for x in range(4):
    thisdict[x]['name'] = (thisdict[x]['name'].replace("æ", "a"))
    thisdict[x]['name'] = (thisdict[x]['name'].replace("¢", "c"))
    thisdict[x]['name'] = (thisdict[x]['name'].replace("ø", "o"))
    thisdict[x]['name'] = (thisdict[x]['name'].replace("ß", "b"))

# for x in range(3):
#     print(thisdict[x]['name'])

# print(thisdict)
######################################################################################

# Só pra saber se cada campo está com o tipo de variável correta
# print(type(thisdict['id']))
# print(type(thisdict['name']))
# print(type(thisdict['quantity']))
# print(type(thisdict['price']))
# print(type(thisdict['category']))
######################################################################################

# Função para adicionar o campo 'quantity' caso ele não exista (QUANTIDADE)
for x in range(4):
    if 'quantity' in thisdict[x]:
        print("Existe")
    else:
        print("Adicionando")
        thisdict[x]["quantity"] = 0

# print(thisdict[3])
######################################################################################

# Função para o valor total dos produtos por categoria, levando em conta sua quantidade
for x in range(4):
    if thisdict[x]['category'] == "Eletrodomésticos":
        totalE = totalE + (thisdict[x]['quantity'] * thisdict[x]['price'])

print(totalE)
######################################################################################
