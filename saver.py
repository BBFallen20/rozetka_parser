import csv

def save(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Модель", "Ссылка", "Цена"])
        for item in items:
            writer.writerow([item['title'], item['link'], item['price']])