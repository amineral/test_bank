from tabulate import tabulate
from datetime import datetime

from config import DATABASE as db
from operations import deposite, withdrawal, add_user
from smart_commands import smart
from bank_help import help

#db = {client : [name, balance, operations[[operation_name, money, date, balance], [operation_name, money, date, balance]], id]}

def client_data(client=None):
    client = input("Введите имя клиента: ")
    if client not in db:
        print("Такого клиента нет в базе.")
        return 0
    else:
        values = []
        headers = ["Имя операции", "Сумма операции", "Дата", "Остаток на счету"]
        operations_list = db[client][2]
        for item in operations_list:
            values.append((item))
        print(client + ": выписка по операциям")
        print(tabulate(values, headers, tablefmt="grid"))
    
def print_database():
    values = []
    headers = ["id", "Имя", "Баланс", "Операции"]
    for data in db:
        operations_list = db[data][2]
        operations = ""
        for item in operations_list:
            operations = operations + "\n" + item[0] + ' | ' + str(item[1]) + "$" + ' | ' + str(item[2])
        id = db[data][3]
        client = db[data][0]
        balance = "$" + str(db[data][1])
        values.append([id, client, balance, operations])
    print(tabulate(values, headers, tablefmt="grid"))


def bank():
    command_list = {
    '--help' : help,
    'add' : add_user,
    'deposite' : deposite,
    'database' : print_database,
    'draw' : withdrawal,
    'client' : client_data,
}
    while True:
        print("\nГлавное меню\n")
        command = input("Введите команду. Введите --help чтобы увидеть список команд или exit чтобы завершить сессию\n>>> ")
        if command == '--exit':
            break
        if command in command_list:
            command_list[command]()
        else:
            print("Неправильная команда")

if __name__ == '__main__':
    bank()