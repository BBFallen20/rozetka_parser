from bs4 import BeautifulSoup
from request import get_html
from requests.exceptions import MissingSchema, InvalidURL
from saver import save


def check_connection(url: str):
    try:
        html_page = get_html(url)
    except MissingSchema:
        print("[X]Connection error.")
        return False
    except InvalidURL:
        print("[X]Invalid url.")
        return False
    connected = True if html_page.status_code == 200 else False
    if connected:
        print("[V]Connection success.")
        return html_page.content
    else:
        print("[X]Connection error.")
        return False


def data_extracting(html):
    soup = BeautifulSoup(html, 'html.parser')
    raw_data = soup.find_all('div', class_='goods-tile__inner')
    cleaned_data = []
    for item in raw_data:
        cleaned_data.append({
            'title': item.find('a', class_='goods-tile__heading')['title'],
            'price': item.find('span', class_='goods-tile__price-value').text.strip(),
            'link': item.find('a', class_='goods-tile__heading')['href']
        })
    return cleaned_data


def main():
    url = input("Enter url to parse:\n")
    connection = check_connection(url)
    if connection:
        cleaned_data = []
        pages = int(BeautifulSoup(connection, 'html.parser').find_all('a', class_='pagination__link')[-1].get_text())
        for page in range(1, pages+1):
            print(f"Page {page} from {pages}")
            page = get_html(url, params={'page': page})
            for item in data_extracting(page.content):
                cleaned_data.append(item)
        path = input("Enter path to save csv file:\n")
        try:
            save(cleaned_data, path)
        except Exception as e:
            print(e)
    else:
        return None


if __name__ == '__main__':
    main()
