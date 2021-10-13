recruit_list = {}

for i in range(5):
    information=input().split(" ")
    recruit_list["{0} {1} {2}".format(*information[:3])]="{0} {1}".format(*information[3:])
print("Фамилия Имя Отчество Год Заболевание")
for key in recruit_list.keys():
    print(key + " " + recruit_list[key])