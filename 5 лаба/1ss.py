import matplotlib.pyplot as plt
import numpy as np
import re


def check_number_format(number):
    regex = r'^[-+]?([1-9]\d*|0)$'
    return re.match(regex, number)


def enter_number(info):
    while True:
        number = input(f"Введите {info}: ")
        if check_number_format(number):
            print("Формат числа верный!")
            return number
        else:
            print("Неверный формат числа. Попробуйте снова.")


a = enter_number("начало 1")
b = enter_number("конец 1")
c = enter_number("шаг 1")

x = np.arange(int(a), int(b), int(c))
y = x**2 - abs(4*x + 5)

plt.plot(x, y, color='g')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(0, 0, color="b")
plt.text(0, 0, "O")
plt.text(-5.43, 10, "y = x**2 - abs(4*x + 5)")
plt.title('Graph of y = x**2 - abs(4*x + 5)')

a = enter_number("начало 2")
b = enter_number("конец 2")
c = enter_number("шаг 2")

x = np.arange(int(a), int(b), int(c))
y = -2 * x**3 - 9 * x**2 + 6
plt.plot(x, y, color='r')
plt.text(-3, 2.4, "y = -2 * x**3 - 9 * x**2 + 6")
plt.grid(True)
plt.show()