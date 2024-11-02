import requests

response = requests.get("https://api.github.com")
print(response)
print("==================\n")
print(response.headers)
print("==================\n")
print(response.status_code)
print("==================\n")
print(response.content)
print("==================\n")
print(response.text)
print("==================\n")
print(response.json())
print("==================\n")
print(response.json()["current_user_url"])

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q":"python"}    
)
print("==================\n")
print(response.status_code)
print("==================\n")
print(response.json())

data = response.json()
print("==================\n")
print(data.keys())
