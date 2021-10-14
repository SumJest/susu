from lab6.modules import task3_module

if not task3_module.input_exist():
    print("Файл с входными данными не обнаружен")
    exit()

n = task3_module.read_n()

prime_numbers = ""

for i in range(2, n + 1):
    if task3_module.is_prime(i):
        prime_numbers += str(i) + " "

task3_module.write_line(prime_numbers)
