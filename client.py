import csv

data_file = "clients.csv"

with open(data_file, 'w', newline='') as csvfile:
    csvfile.write('')

print("Здравствуйте! Введите данные:")

while True:
    name = input('Имя:')
    if name == 'stop':
        break

    surname = input('Фамилия:')
    birthday = input('Дата рождения:')
    bonuses = input('Начислено бонусов:')

    new_client = {
        'Name': name,
        'Surname': surname,
        'Birthday': birthday,
        'Bonuses': bonuses
    }

    with open(data_file, 'a', newline='') as csvfile:
        field_names = ['Name', 'Surname', 'Birthday', 'Bonuses']
        csvwriter = csv.DictWriter(csvfile, fieldnames=field_names)

        if csvfile.tell() == 0:
            csvwriter.writeheader()
            csvwriter.writerow(new_client)

    print(f"Клиент {name} {surname} добавлен!")
