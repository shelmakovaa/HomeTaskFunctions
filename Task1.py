# перечень всех документов

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

#перечень полок, на которых хранятся документы
#(если документ есть в documents, то он обязательно должен быть и в directories)
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


#Пункт 1. Пользователь по команде "p" может узнать владельца документа по его номеру
def get_owner_name(doc_number):
    for data in documents:
        if data.get('number') == doc_number:
            return f"Владелец документа: {data.get('name')}"
    return "Документ не найден в базе"


#Пункт 2. Пользователь по команде "s" может по номеру документа узнать на какой полке он хранится
def get_shelf(doc_number):
    for directory, data in directories.items():
        if doc_number in data:
            return f"Документ хранится на полке: {directory}"
    return "Документ не найден в базе"


#Пункт 3. Пользователь по команде "l" может увидеть полную информацию по всем документам
def get_all_data():
    for data in documents:
        print(f"№: {data.get('number')}, тип: {data.get('type')}, владелец: {data.get('name')}, "
              f"полка хранения: {''.join(c for c in get_shelf(data.get('number')) if c.isdigit())}")


#Пункт 4. Пользователь по команде "ads" может добавить новую полку
def check_shelf(shelf_number):
    if shelf_number in directories.keys():
        return True
    return False


def shelf_list():
    return f"{', '.join(str(directory) for directory in directories.keys())}."


def add_shelf(shelf_number):
    if not check_shelf(shelf_number):
        directories[shelf_number] = []
        return (f"Полка добавлена. Текущий перечень полок: {shelf_list()}")
    return (f"Такая полка уже существует. Текущий перечень полок: {shelf_list()}")


#Пункт 5. Пользователь по команде "ds" может удалить существующую полку из данных (только если она пустая)
def delete_shelf(shelf_number): #проверяем наличие полки
    if not check_shelf(shelf_number):
        return f"Такой полки не существует. Текущий перечень полок: {shelf_list()}"
    else:
        if directories[shelf_number] == []:
            del directories[shelf_number]
            return f"Полка удалена. Текущий перечень полок:{shelf_list()}"
        return f"На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {shelf_list()}"


def get_user_input():
        print("p - узнать владельца документа по его номеру")
        print("s - по номеру документа узнать на какой полке он хранится")
        print("l - увидеть полную информацию по всем документам")
        print("ads - добавить новую полку")
        print("ds - удалить существующую полку из данных")
        print("q - выход")
        return input("Введите команду: ")


def main():
    while True:
        choose = get_user_input()
        commands = ['s', 'p', 'l', 'ads', 'ds']
        if choose == 'q':
            break
        if choose not in commands:
            print("Неизвестная команда\n")
        if choose == 'p':
            print(get_owner_name(input("Введите номер документа: ")))
            print("\n")
        if choose == 's':
            print(get_shelf(input("Введите номер документа: ")))
            print("\n")
        if choose == 'l':
            get_all_data()
            print("\n")
        if choose == 'ads':
            print(add_shelf(input("Введите номер полки: ")))
            print("\n")
        if choose == 'ds':
            print(delete_shelf(input("Введите номер полки: ")))
            print("\n")

main()

