from operations import deposite, withdrawal, add_user

def smart():
    while True:
        command = input(">>> ")
        if command == "exit":
            break
        params = parse_command(command.split())
        args = None
        if check_parse(params["command"], args[:1]):
            if params["command"] == "add":
                add_user(name=args[1])
        
def check_parse(command, args):
    params = {
        "add" : ["name"],
        "depo" : ["name", "summ", "desc"],
    } 
    if command in params:
        for i in params[command]:
            if i not in params[command]:
                return False
    return True

def parse_command(command):
    main = command.pop(0)
    params = {}
    params["command"] = main
    for item in command:
        p = item.split("=")
        params[p[0]] = p[1]

    return params

if __name__ == '__main__':
    smart()