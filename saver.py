import csv


def save(items: list, path: str):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([row_name for row_name in items[0].keys()])
        for item in items:
            writer.writerow([item['title'], item['link'], item['price']])
