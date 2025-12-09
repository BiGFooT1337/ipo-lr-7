# Гаркин Вадим
import json

# Открываем файл dump.json для чтения
with open("dump.json", "r", encoding="utf-8") as f:
    data = json.load(f)  # Загружаем данные из файла в переменную data

skills = []  # Создаём пустой список для хранения навыков

# Проходим по всем элементам в загруженных данных
for item in data:
    # Проверяем, что элемент относится к модели "data.skill"
    if item.get("model") == "data.skill":
        # Извлекаем код и название навыка
        code = item["fields"]["code"]
        title = item["fields"]["title"]
        # Добавляем навык в список в виде словаря
        skills.append({"code": code, "title": title})

print("start code ...")  # Сообщение о начале работы программы

# Просим пользователя ввести номер квалификации и убираем пробелы по краям
user_code = input("Введите номер квалификации: ").strip()

chain = []  # Создаём список для подходящих навыков

# Проверяем каждый навык из списка skills
for skill in skills:
    skill_code = skill["code"]
    # Если введённый код совпадает с кодом навыка ИЛИ начинается с кода навыка + "-"
    if user_code == skill_code or user_code.startswith(skill_code + "-"):
        chain.append(skill)  # Добавляем подходящий навык в цепочку

# Сортируем навыки по длине кода (от коротких к длинным)
chain.sort(key=lambda x: len(x["code"]))

seen = set()        # Создаём множество для отслеживания уже добавленных кодов
unique_chain = []  # Список для уникальных навыков

# Удаляем дубликаты по коду навыка
for skill in chain:
    if skill["code"] not in seen:  # Если код ещё не встречался
        unique_chain.append(skill)  # Добавляем навык в результат
        seen.add(skill["code"])      # Запоминаем код навыка

# Выводим результат
if unique_chain:
    print("============== Найдено ==============")
    # Для каждого найденного навыка выводим код и название
    for skill in unique_chain:
        print(f"{skill['code']} >> {skill['title']}")
else:
    print("============== Не найдено ==============")

print("... end code")  # Сообщение об окончании работы программы
