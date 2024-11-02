import requests

# abri webhook.site
url = "https://webhook.site/473530f2-e9cb-4755-ae84-946df6f0c86a"
payload = {"plato": "pasta", "cantidad": 2}
query_params = {"nombre": "Salva"}
response = requests.post(url, data=payload, params=query_params)
print(response.status_code)

print(response.text)
# print(response.json()) # esto es un error