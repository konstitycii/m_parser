import requests
from bs4 import BeautifulSoup

url = "https://www.profinance.ru/currency_usd.asp"

# Отправляем запрос на получение HTML-кода страницы
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Используем BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим нужный элемент на странице (в данном случае, первый элемент с классом "cell")
    value_element = soup.find("td", class_="cell")

    if value_element:
        # Извлекаем текст из элемента
        value = value_element.text.strip()

        print("Значение:", value)
    else:
        print("Элемент не найден")
else:
    print("Ошибка при запросе:", response.status_code)
