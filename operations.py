from datetime import datetime

from config import DATABASE as db

def deposite(name=None, desc=None, summ=None):
    if not name:
        name = input("Введите имя клиента: ")
    if name in db:
        if not desc:
            desc = input("Введите название операции: ")
        if not summ:
            try:
                summ = int(input("Сколько положить на счет?: "))
            except ValueError:
                return(print("-----\nОшибка! Неправильная сумма\n-----"))

        date = datetime.now()
        db[name][1] += summ
        db[name][2].append([desc, summ, date, db[name][1]])
        print("Операция успешна\n")
    else:
        print("Такого клиента нет в базе.")

def withdrawal(name=None, desc=None, summ=None):
    if not name:
        name = input("Введите имя клиента: ")
    if name in db:
        if not desc:
            desc = input("Введите название операции: ")
        if not summ:
            try:
                summ = int(input("Сколько списать?: "))
            except ValueError:
                return(print("-----\nОшибка! Неправильная сумма\n-----"))

        if db[name][1] - summ < 0:
            print("У вас недостаточно средств на счету для совершения операции.")
            print("Операция не может быть осуществлена.")
            return 0
        else:
            date = datetime.now()
            db[name][1] -= summ 
        db[name][2].append([desc, -summ, date, db[name][1]])
        print("Операция успешна!\n")

def add_user(name=None):
    if not name:
        print("\nДобавление нового клиента. Введите back чтобы вернуться в главное меню")
        name = input("Введите имя клиента: ")
    if name == 'back':
        return None
    if name not in db:
        id = len(db) + 1
        balance = 0
        operations = []
        client = name
        db[name] = [client, balance, operations, id]
        print(f"Операция успешна! Новый клиент {name} добавлен.\n")
    else:
        print("Такой клиент уже существует.\n")


if __name__ == '__main__':
    add_user()