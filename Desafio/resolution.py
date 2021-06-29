import json


def ler_json():
    with open('broken-database.json', 'r', encoding='utf8') as f:
        return json.load(f)

# def ler_json():
#     with open('broken-database.json', 'r', encoding='utf8') as f:
#         return json.load(f)


data = ler_json()


def salva_json(dados):
    with open('certo-database.json', 'w', encoding='utf8') as f:
        return json.dump(dados, f)


salva_json(data)

prod0 = data[0]
prod1 = data[1]
prod2 = data[2]
prod3 = data[3]
prod4 = data[4]
prod5 = data[5]
prod6 = data[6]
prod7 = data[7]
prod8 = data[8]
prod9 = data[9]

# x = prod0.values()

# prod0["quantity"] = 22

print(type(prod0))

# def arruma_nome(errado):

#     name_certo = (errado.replace("æ","a"))
#     name_certo = (name_certo.replace("¢","c"))
#     name_certo = (name_certo.replace("ø","o"))
#     name_certo = (name_certo.replace("ß","b"))

# print(name_certo)

# nome_errado = input()

# arruma_nome(data)
