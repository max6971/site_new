import requests

url = 'https://jsonplaceholder.typicode.com/posts'

params = {
    'userId': 1
}

response = requests.get(url, params=params)

# Проверка успешности запроса
if response.status_code == 200:
    # Получение данных в формате JSON
    data = response.json()

    # Распечатка записей
    for record in data:
        print(record)
else:
    print(f"Ошибка: {response.status_code}")