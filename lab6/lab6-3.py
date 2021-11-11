from lab6.modules import calculator, my_module

calc = calculator.Calculator()  # создать новый экземпляр класса Calculator, определенный в модуле calculator

calc.add(2)
print(calc.get_current())

# Импортируйте модуль my_module и используйте функцию hello_world.

my_module.hello_world("Roman")  # Вызовите функцию hello_world из модуля my_module

# ----------------------------------------------------#


""" 
Python поставляется с библиотекой стандартных модулей. 
Запомните, что вы можете использовать Ctrl + Space после точки (.), чтобы изучить доступные методы модуля. 
"""

import datetime

current_date = datetime.datetime.now()
print(datetime.datetime.strftime(current_date,"%d.%m.%Y %H:%M:%S"))  # Выведите текущую дату, используя встроенный модуль datetime

# ----------------------------------------------------#


""" 
Специальная форма оператора импорта импортирует имена из модуля непосредственно в таблицу символов импортирующего модуля. 
Таким образом, вы можете использовать функции напрямую без префикса module_name. 
"""

from lab6.modules.calculator import Calculator

calc = Calculator()  # теперь мы можем использовать класс Calculator без префикса calculator.
calc.add(2)
print(calc.get_current())

# Импортируйте функцию hello_world из модуля my_module.Сравните с предыдущим примером.
from lab6.modules.my_module import hello_world

print(hello_world("Roman"))  # Функция hello_world должна вызываться без указания модуля
# (Функция не возращает значения)

