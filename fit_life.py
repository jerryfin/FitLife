# Проект FitLife - MVP версия 1.0


# 1. Знакомство
user_name = input('Пожалуйста введите ваше имя: ').title()

# Запись возраста в переменную user_age
while True:
    try:
        user_age = int(input('Введите ваш возраст: '))
        if user_age <= 0:
            print('Рост должен быть больше нуля')
            continue
        break
    except ValueError:
        print('Вы ввели некорректный возраст')

# 2. Сбор данных
# Запись веса в переменную user_weight
while True:
    try:
        user_weight = float(input('Укажите ваш вес: '))
        if user_weight <= 0:
            print('Вес должен быть больше нуля')
            continue
        break
    except ValueError:
        print('Вы ввели некорректный вес')

# Запись роста в переменную user_height
while True:
    try:
        user_height = float(input('Ваш рост в метрах (например, 1.75): '))
        if user_height < 0:
            print('Вы ввели отрицательное значение')
            continue
        elif user_height > 2.5:
            print('Пожалуйста укажите рост в метрах')
            continue
        break
    except ValueError:
        print('Вы ввели некорректный рост')


# Расчет индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# Расчет рекомендуемого количества воды в день
WATER_PER_KG = 30
water_needed = (user_weight * WATER_PER_KG / 1000)

# 4. Вывод
print()
print(f'Привет, {user_name}!')
print(f'Возраст: {user_age}')
print(f'ИМТ: {bmi}')
print(f"Рекомендуемая норма воды: {water_needed:.1f} л. в день")
print("Расчет окончен. Будьте здоровы!")
