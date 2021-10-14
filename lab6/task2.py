import os

txt_amount = 0
input_file_exist = False

for file in os.listdir(os.getcwd() + "\\lab6"):
    if file.endswith(".txt"):
        txt_amount += 1
        if file == "input.txt":
            input_file_exist = True

if not input_file_exist:
    print("Файл с входными данными не обнаружен")
    exit()

f = open("lab6/input.txt", 'r')
number = int(f.readline().split(' ')[0])
f.close()

proizv = 1
summ = 0
amount = 0

num = number
while num > 0:
    amount += 1
    digit = num % 10
    summ += digit
    proizv *= digit
    num //= 10

f = open("lab6/output.txt", 'w')

f.write(f"Число: {number}\nКоличество цифр: {amount}\nСумма цифр: {summ}\nПроизведение цифр: {proizv}")
