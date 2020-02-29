import requests


# Я НЕ БОТ
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0', 'accept': '*/*'}
# Получаем Html страницу с ссылки
def get_html(url, params=None):
    r = requests.get(url=url, headers=HEADERS, params=params)
    return r



