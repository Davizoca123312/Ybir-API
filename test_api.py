import requests

url = "http://localhost:5000/analyze"
data = {"text": "Estou muito feliz com o seu serviço!"}

response = requests.post(url, json=data)
if response.status_code == 200:
    result = response.json()
    print("Sentimento:", result["sentiment"])
else:
    print("Erro:", response.status_code, response.text)
