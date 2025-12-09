# Гаркин Вадим, Вариант 5
import json
import os

FILENAME = "cities.json"  # Имя файла с данными о городах

print("start code ...")

# Загрузка данных из файла
cities = []
if os.path.exists(FILENAME):
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            cities = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка при загрузке данных: {e}")

operation_count = 0

while True:
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю id")
    print("3. Добавить запись")
    print("4. Удалить запись по полю id")
    print("5. Выйти из программы")

    choice = input("Выберите пункт меню (1–5): ").strip()

    if choice == "1":
        # Вывод всех городов
        print("\n============== Все записи ==============")
        if not cities:
            print("Нет записей.")
        else:
            for city in cities:
                is_big_str = "большой (>100 000)" if city["is_big"] else "маленький (≤100 000)"
                print(f"ID: {city['id']}")
                print(f"Название: {city['name']}")
                print(f"Страна: {city['country']}")
                print(f"Статус: {is_big_str}")
                print(f"Население: {city['people_count']}")
                print("-" * 40)
        operation_count += 1

    elif choice == "2":
        # Поиск города по ID
        while True:
            try:
                target_id = int(input("Введите ID города: ").strip())
                if target_id <= 0:
                    print("Ошибка: ID должен быть положительным числом.")
                    continue
                break
            except ValueError:
                print("Ошибка: введите целое число.")

        found = False
        for index, city in enumerate(cities):
            if city["id"] == target_id:
                print(f"\n============== Найдено ==============")
                print(f"Позиция в списке: {index + 1}")
                is_big_str = "большой (>100 000)" if city["is_big"] else "маленький (≤100 000)"
                print(f"ID: {city['id']}")
                print(f"Название: {city['name']}")
                print(f"Страна: {city['country']}")
                print(f"Статус: {is_big_str}")
                print(f"Население: {city['people_count']}")
                found = True
                break
        if not found:
            print("\n============== Не найдено ===============")
        operation_count += 1

    elif choice == "3":
        # Добавление нового города
        new_id = max([c["id"] for c in cities], default=0) + 1

        # Ввод названия города
        while True:
            name = input("Введите название города: ").strip()
            if name:
                break
            print("Ошибка: поле не может быть пустым.")

        # Ввод страны
        while True:
            country = input("Введите страну: ").strip()
            if country:
                break
            print("Ошибка: поле не может быть пустым.")

        # Ввод численности населения
        while True:
            try:
                people_count = int(input("Введите численность населения: ").strip())
                if people_count <= 0:
                    print("Ошибка: значение должно быть положительным.")
                    continue
                break
            except ValueError:
                print("Ошибка: введите целое число.")

        # Определение статуса is_big
        is_big = people_count > 100000

        # Создание и добавление новой записи
        new_city = {
            "id": new_id,
            "name": name,
            "country": country,
            "is_big": is_big,
            "people_count": people_count
        }
        cities.append(new_city)

        # Сохранение в файл
        try:
            with open(FILENAME, "w", encoding="utf-8") as f:
                json.dump(cities, f, ensure_ascii=False, indent=4)
            print("Запись успешно добавлена.")
        except IOError as e:
            print(f"Ошибка при сохранении данных: {e}")
        operation_count += 1

    elif choice == "4":
        # Удаление города по ID
        while True:
            try:
                target_id = int(input("Введите ID города для удаления: ").strip())
                if target_id <= 0:
                    print("Ошибка: ID должен быть положительным числом.")
                    continue
                break
            except ValueError:
                print("Ошибка: введите целое число.")

        initial_len = len(cities)
        cities[:] = [c for c in cities if c["id"] != target_id]

        if len(cities) == initial_len:
            print("\n============== Не найдено ===============")
        else:
            # Сохранение после удаления
            try:
                with open(FILENAME, "w", encoding="utf-8") as f:
                    json.dump(cities, f, ensure_ascii=False, indent=4)
                print("Запись успешно удалена.")
            except IOError as e:
                print(f"Ошибка при сохранении данных: {e}")
        operation_count += 1

    elif choice == "5":
        print(f"\nВыполнено операций: {operation_count}")
        print("... end code")
        break

    else:
        print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")
