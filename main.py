import json
import csv
import random

game_state = {
    "location": "start",
    "inventory": set(),
}

def save_game_data():
    game_data = {
        "location": game_state["location"],
        "inventory": list(game_state["inventory"]),
    }
    with open("game_data.json", "w") as file:
        json.dump(game_data, file)

def load_game_data():
    try:
        with open("game_data.json", "r") as file:
            saved_data = json.load(file)
            game_state.update(saved_data)
            print("Загружены сохраненные данные.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Файл сохраненных данных не найден или содержит некорректные данные. Создан новый файл.")

def delete_game_data():
    if input("Вы уверены, что хотите удалить сохраненные данные? (да/нет): ").strip().lower() == "да":
        with open("game_data.json", "w") as file:
            json.dump({}, file)
        game_state.clear()
        print("Сохраненные данные удалены.")

def write_game_data_to_csv():
    with open("game_data.csv", "w", newline="") as csvfile:
        fieldnames = ["location", "inventory"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(game_state)
        print("Данные записаны в CSV файл.")

def main():
    player_name = input("Введите ваше имя: ")
    print(f"Добро пожаловать на Загадочный остров, {player_name}!")

    load_game_data()

    print("Вы находитесь на берегу острова и перед вами три пути.")
    print("1. Пойти в глубь леса\n2. Пойти к горам\n3. Поплыть на лодке в неизведанные воды")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2/3): "))
        if choice in [1, 2, 3]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        forestgump()
    elif choice == 2:
        mountains()
    elif choice == 3:
        sea()

    save_game_data()
    write_game_data_to_csv()

def forestgump():
    print("Вы отправились в глубь леса.")
    print("1. Пойти к зданию.\n2. Пойти к ручью")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        build()
    elif choice == 2:
        stream()

def build():
    print("Вы пришли к заброшенному зданию.")
    print("Вы видите загадочную дверь с замком.")
    print("1. Попытаться открыть дверь.\n2. Вернуться обратно в лес")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        if random.random() < 0.5:
            print("Поздравляем! Вы нашли сокровище!")
            game_state["inventory"].add("сокровище")
        else:
            print("К сожалению, дверь закрыта на замок и вы не можете ее открыть.")
    elif choice == 2:
        forestgump()

def stream():
    print("Вы подошли к ручью и заметили мост через него.")
    print("1. Перейти мост.\n2. Вернуться обратно в лес")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        print("Вы успешно перешли мост и продолжили свое приключение.")
        cave()
    elif choice == 2:
        forestgump()

def mountains():
    print("Вы решили отправиться к горам.")
    print("Вы поднимаетесь в горы и видите темную пещеру.")
    print("1. Зайти в пещеру.\n2. Пойти в обход пещеры")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        cave()
    elif choice == 2:
        around_cave()

def cave():
    print("Вы вошли в темную пещеру.")
    print("1. Пойти налево.\n2. Пойти направо")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        print("Вы нашли сокровище! Поздравляем, вы победили игру!")
        game_state["inventory"].add("сокровище")
    elif choice == 2:
        print("Вы наткнулись на большого медведя и погибли. Игра окончена.")

def around_cave():
    print("Вы решили обойти пещеру.")
    print("1. Взять драгоценный камень.\n2. Продолжить исследование гор")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        print("Поздравляем! Вы нашли драгоценный камень и победили игру!")
        game_state["inventory"].add("драгоценный камень")
    elif choice == 2:
        print("Вы продолжаете исследование гор, но больше ничего не находите.")

def sea():
    print("Вы решаете поплыть на лодке в неизведанные воды.")
    print("Ваша лодка терпит кораблекрушение на неизведанном острове.")
    print("1. Исследовать остров.\n2. Попытаться починить лодку и вернуться")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        print("Вы исследуете остров и находите сокровище. Поздравляем, вы победили игру!")
        game_state["inventory"].add("сокровище")
    elif choice == 2:
        print("Вы пытаетесь починить лодку, но безуспешно. Игра окончена.")

if __name__ == "__main__":
    main()
    if input("Желаете удалить сохраненные данные? (да/нет): ").strip().lower() == "да":
        delete_game_data()