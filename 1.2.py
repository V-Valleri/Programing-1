"""
Задача №2.

Потрібно підрахувати, на скільки раніше буде закінчуватися k-й урок,
якщо всі перерви скоротити на 5 хвилин. Вводиться одне натуральне число k,
не більше 7. Необхідно вивести одне натуральне число - час у хвилинах.

Автор: Костючик Валерія Дмитрівна
"""

k = int(input("Введіть номер уроку (не більше 7): "))

t_ur = 45
t_per = [5, 10, 20, 10, 10, 5, 10]


s_t_ur = (k - 1) * t_ur
s_t_per = sum(t_per[:k - 1])

t = s_t_ur + s_t_per

new_t = t - (5 * (k - 1))

print("Загальний час у хвилинах після скорочення перерв на 5 хвилин:", new_t)
