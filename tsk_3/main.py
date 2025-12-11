import json
import os

FILENAME = "cities.json"


def load_data(filename):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            raw = f.read().strip()
            if raw == "":
                return []
            data = json.loads(raw)
            if not isinstance(data, list):
                return []
            return data
    except Exception as e:
        print("Ошибка при загрузке:", e)
        return []


def save_data(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print("Ошибка при сохранении:", e)
        return False


def input_nonempty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Поле не может быть пустым.")


def input_positive_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v > 0:
                return v
            print("Число должно быть положительным.")
        except ValueError:
            print("Введите целое число.")


def show_all(cities):
    print("\n=== Все записи ===")
    if not cities:
        print("Нет записей.")
        return
    for c in cities:
        print(f"ID: {c.get('id')} | {c.get('name')} ({c.get('country')}) — {c.get('people_count')} чел.")
    print("==================")


def show_by_id(cities):
    tid = input_positive_int("Введите ID города: ")
    for i, c in enumerate(cities):
        if c.get("id") == tid:
            print("\n=== Найдено ===")
            print(f"Позиция: {i+1}")
            print(json.dumps(c, ensure_ascii=False, indent=4))
            return
    print("Не найдено.")


def add_city(cities):
    new_id = max((c.get("id", 0) for c in cities), default=0) + 1
    name = input_nonempty("Введите название города: ")
    country = input_nonempty("Введите страну: ")
    people = input_positive_int("Введите численность населения: ")
    city = {
        "id": new_id,
        "name": name,
        "country": country,
        "is_big": people > 100000,
        "people_count": people
    }
    cities.append(city)
    if save_data(FILENAME, cities):
        print("Город добавлен.")
    else:
        print("Не удалось сохранить.")


def delete_city(cities):
    # Удаляет город по ID и сразу сохраняет файл
    tid = input_positive_int("Введите ID города для удаления: ")
    initial = len(cities)
    # убедимся, что сравниваем числа
    cities[:] = [c for c in cities if int(c.get("id", 0)) != tid]
    if len(cities) == initial:
        print("Не найдено — удаление не выполнено.")
    else:
        if save_data(FILENAME, cities):
            print("Запись успешно удалена.")
        else:
            print("Запись удалена в памяти, но не удалось сохранить файл.")


def main():
    print("start code ...")
    cities = load_data(FILENAME)
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
            show_all(cities)
            operation_count += 1
        elif choice == "2":
            show_by_id(cities)
            operation_count += 1
        elif choice == "3":
            add_city(cities)
            operation_count += 1
        elif choice == "4":
            delete_city(cities)
            operation_count += 1
        elif choice == "5":
            print(f"\nВыполнено операций: {operation_count}")
            print("... end code")
            break
        else:
            print("Некорректный выбор. Введите 1–5.")


if __name__ == "__main__5":
    main()