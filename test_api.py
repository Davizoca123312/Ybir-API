import requests



    # para um texto simples

# url = "http://localhost:8000/analyze"
# data = {"text": "Mano, não aguento mais esse calorrrr"}

# response = requests.post(url, json=data)
# if response.status_code == 200:
#     result = response.json()
#     print(result)
# else:
#     print("Erro:", response.status_code, response.text)


    #para uma lista de textos
url = "http://localhost:8000/rank"

textos = [
    "Comprei esse fone Bluetooth e me surpreendi! A qualidade do som é excelente e a bateria dura muito.",
    "O aspirador é bonito, mas não tem força nenhuma. Me arrependi da compra.",
    "Produto chegou antes do prazo, muito bem embalado. Ainda não testei, mas até agora tudo certo.",
    "Veio com defeito e o suporte da loja é péssimo. Não recomendo.",
    "Simplesmente perfeito! Cumpre exatamente o que promete e ainda vem com brindes."
]
data = {"texts": textos}
response = requests.post(url, json=data)
if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print("Erro:", response.status_code, response.text)