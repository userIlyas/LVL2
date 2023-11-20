def create():
    n = int(input("Введите число записей в словаре: "))
    slot = {}
    for i in range(n):
        flag = True
        while flag:
            info = str(input("Введите строку в словарь: "))
            if " - " in info:
                key, value = info.split(" - ")
                if key not in slot:
                    slot[key] = value
                    flag = False
                else:
                    flag = True
            else:
                flag = True
    return slot


def search(slot):
    name = str(input("Введите запрос: "))
    if name in slot:
        print(slot[name])
    else:
        print("Нет в словаре!")


def main():
    search(create())


if __name__ == "__main__":
    main()