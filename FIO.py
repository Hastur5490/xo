import csv
with open('FIOandTelephone.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fio = input("ФИО: ")
    for obj in reader:
        if obj['\ufeffFIO'] == fio:
            print(obj['Telephone'])