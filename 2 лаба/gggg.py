while True:
    try:
        n = int(input("Введите целое число(!=0): "))
        break
    except ValueError:
        print("Целое число!")

if n == 0:
    print("Пока")
    exit()

birthdays = {}

for i in range(n):
    while True:
        try:
            combo = input('Введите в формате(имя, день, месяц или день, месяц, имя): ')
            if combo[0].isdigit():
                day, month, name = combo.split()
            else:
                name, day, month = combo.split()

            day = int(day)
            break
        except ValueError:
            print("Целое число!")
    if month not in birthdays:
        birthdays[month] = []
    birthdays[month].append((name, day))

requested_month = input("введите месяц ")

if requested_month in birthdays:
    for name, day in birthdays[requested_month]:
        print(name, day)
else:
    print("ДР в этот месяц нет")
