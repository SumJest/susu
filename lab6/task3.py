from lab6.modules import task3_module

if not task3_module.input_exist():
    print("Файл с входными данными не обнаружен")
    exit(0)

count = task3_module.read_n()

list_of_integers = list(range(2, count))

prime_numbers = task3_module.prime_filter(list_of_integers)

output = " ".join(
    map(str, prime_numbers))  # преобразовываем числа в списке в строковый формат и заполняем строку элементами

task3_module.write_line(output)  # выводим в файл
