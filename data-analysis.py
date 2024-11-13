import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Функція для обчислення віку
def calculate_age(birthdate):
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

gender_counts = {'Чоловіча': 0, 'Жіноча': 0}
age_categories = {'<18': 0, '18-45': 0, '45-70': 0, '>70': 0}

with open('employees.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаємо заголовок
    for row in reader:
        gender = row[3]
        birth_date = datetime.strptime(row[4], '%Y-%m-%d')
        age = calculate_age(birth_date)  # Тепер функція визначена

        # Оновлюємо підрахунок статі
        gender_counts[gender] += 1

        # Оновлюємо підрахунок вікових категорій
        if age < 18:
            age_categories['<18'] += 1
        elif 18 <= age <= 45:
            age_categories['18-45'] += 1
        elif 45 <= age <= 70:
            age_categories['45-70'] += 1
        else:
            age_categories['>70'] += 1

# Створення графіку для статі
plt.bar(gender_counts.keys(), gender_counts.values())
plt.title('Розподіл за статтю')
plt.show()

# Створення графіку для вікових категорій
plt.bar(age_categories.keys(), age_categories.values())
plt.title('Розподіл за віковими категоріями')
plt.show()
