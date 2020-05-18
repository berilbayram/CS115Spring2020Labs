from private import Private
from state import State

file = open("doctor_data.txt", "r")
li = file.readlines()
l = []
for i in range(len(li)):
    l.append(li[i].split(";"))
doctors = []
for i in range(len(l)):
    if len(l[i]) == 4:
        doctor = Private(l[i][0], l[i][1], float(l[i][2]), float(l[i][3]))
        if doctor not in doctors:
            doctors.append(doctor)
        else:
            print(str(doctor) + " not added, duplicate!")
    else:
        doctor = State(l[i][0], l[i][1], float((l[i][2])))
        if doctor not in doctors:
            doctors.append(doctor)
        else:
            print(str(doctor) + " not added, duplicate!")
sorted_list = []

while len(doctors) != 0:
    boss = doctors[0]
    for i in range(0, len(doctors)):
        if not doctors[i] < boss:
            boss = doctors[i]
    sorted_list.append(boss)
    doctors.remove(boss)

for i in range(len(sorted_list)-1, -1, -1):
    print(sorted_list[i])






