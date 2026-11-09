import requests

r = requests.get("https://dadosabertos.camara.leg.br/api/v2/deputados?itens=1", timeout=30)

print("retorno API status:", r.status_code)