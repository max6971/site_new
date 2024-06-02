import requests

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post(url, json=data)

print(f"Статус-код: {response.status_code}")
print("Содержимое ответа:")
print(response.json())