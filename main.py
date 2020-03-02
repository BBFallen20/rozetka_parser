from bs4 import BeautifulSoup
from request import get_html
from saver import save
import os
import time
# Адресс страницы 'https://hard.rozetka.com.ua/videocards/c80087/' https://hard.rozetka.com.ua/motherboards/c80082/


# Главная функция
def parse(url):
    # Получаем html
    page = get_html(url)
    if page.status_code == 200:
        print('='*50)
        print('[+]Connected.')
        print('=' * 50)
        hardware = []
        pages = get_pages(page.text)
        for page in range(1, pages+1):
            print(f'Info checking {page} from {pages}')
            page = get_html(url, params={'page': page})
            hardware.extend(content(page.text))
        print(f'''{'='*50}
\t\t\t\tReady!
Finded: {len(hardware)} products.
{'='*50}''')
        path = input("Enter way to save the file:\n")+'\hardware.csv'
        try:
            save(hardware, path)
            print('='*50)
            print('Saved.(hardware.csv)')
            print('='*50)
            time.sleep(1.5)
            os.startfile(path)
        except:
            print("Failed to save to the path.")
    else:
        print('='*50)
        print('[!]Connection error.')
        print('=' * 50)


def get_pages(page):
    soup = BeautifulSoup(page, 'html.parser')
    pagination_item = soup.find_all('a', class_='pagination__link')
    if pagination_item:
        return int(pagination_item[-1].get_text())
    else:
        return 1



def content(page):
    soup = BeautifulSoup(page, 'html.parser')
    # Парсим все карточки из каталога
    cards = soup.find_all('div', class_='goods-tile__inner')
    # Словарь для итоговых значений
    videocards = []
    # Циклом проходимся по всем карточкам,собирая инфу
    for card in cards:
        videocards.append({ # Добавляем в словарь
            'title': card.find('span', class_='goods-tile__title').get_text(strip=True), # Название товара
            'link': card.find('a', class_='goods-tile__heading',).get('href'), # СсылОЧКА
            'price': card.find('span', class_='goods-tile__price-value',).get_text(strip=True), # СсылОЧКА

        })
    return videocards


print("="*50)
print("\t\t\tRozetka parser v2.0")
print("="*50)
while True:
    mode = input('''Choose what to do:
1.Parse videocards.
2.Parse motherboards.
3.Parse RAM.
4.Parse CPU.
5.Your link.
6.Exit.\n''')
    if mode == '1':
        url = 'https://hard.rozetka.com.ua/videocards/c80087/'
        parse(url)
    elif mode == '2':
        url = 'https://hard.rozetka.com.ua/motherboards/c80082/'
        parse(url)
    elif mode == '3':
        url = 'https://hard.rozetka.com.ua/memory/c80081/'
        parse(url)
    elif mode == '4':
        url = 'https://hard.rozetka.com.ua/processors/c80083/'
        parse(url)
    elif mode == '5':
        url = input(
            'Enter link to rozetka with ""\n(EXAMPLE:"https://hard.rozetka.com.ua/videocards/c80087/"):\n').replace('"',
                                                                                                                    '')
        try:
            parse(url)
        except Exception:
            print("Error with link connection.")
            continue
    elif mode == '6':
        exit()
    else:
        print("Unknown command.")
        continue