# Вводим все целочисленные значения времени
Hotp = int(input())
Motp = int(input())
Hp = int(input())
Mp = int(input())

# Считаем минуту прибытия
Mpr = (Motp + Mp) % 60
# Считаем час прибытия
Hpr = (Hotp + Hp + (Motp + Mp) // 60) % 24
# Считаем количество суток, с учетом отсутсвия ограничений на величину минут
days = (Hp + Mp//60) // 24

# Форматируем целочисленное значение до 2 цифр с добавлением незначаших нулей
print("{:02d} hours : {:02d} minutes".format(Hpr, Mpr))
print(str(days) + " days")
