name = input("Enter your name: ")
surname = input("Enter your surname: ")
group = input("Enter your group: ")

print("Привет, %s %s из группы %s!" % (name, surname, group))
email = input("Введи свою электронную почту? ")
print((surname[:5] + (name[:5]) * 2 + (email[:5]) * 3).lower())


