import csv
from faker import Faker

fake = Faker(locale='uk_UA')

# Словник по батькові для чоловіків та жінок
patronymics_male = ['Іванович', 'Петрович', 'Сергійович', 'Андрійович', 'Тарасович', 'Павлович', 'Антонович', 'Данилович',
                    'Олександрович', 'Олексійович', 'Артемович', 'Кирилович', 'Назарович', 'Михайлович', 'Романович',
                    'Тимофійович', 'Тимурович', 'Янович', 'Богданович', 'Денисович']
patronymics_female = ['Іванівна', 'Петрівна', 'Сергіївна', 'Андріївна', 'Тарасівна', 'Павлівна', 'Антонівна', 'Данилівна',
                      'Олександрівна', 'Олексіївна', 'Артемівна', 'Кирилівна', 'Назарівна', 'Михайлівна', 'Романівна',
                      'Тимофіївна', 'Тимурівна', 'Янівна', 'Богданівна', 'Денисівна']

with open('employees.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто', 'Адреса', 'Телефон', 'Email'])

    for _ in range(2000):
        gender = 'Чоловіча' if fake.random_element(['Чоловіча', 'Жіноча']) == 'Чоловіча' else 'Жіноча'
        first_name = fake.first_name_male() if gender == 'Чоловіча' else fake.first_name_female()
        patronymic = fake.random_element(patronymics_male) if gender == 'Чоловіча' else fake.random_element(
            patronymics_female)
        birth_date = fake.date_of_birth(minimum_age=15, maximum_age=86)

        # Генерація інших даних (посада, місто тощо)
        # Запис у CSV
        writer.writerow(
            [fake.last_name(), first_name, patronymic, gender, birth_date, fake.job(), fake.city(), fake.address(),
             fake.phone_number(), fake.email()])
