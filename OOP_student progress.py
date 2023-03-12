import re


class Student:
    def __init__(self, full_name, group_number, grades):
        self.full_name = full_name
        self.group_number = group_number
        self.grades = grades

    def __str__(self):
        txt = 'Student:' + self.full_name + ' from group number ' + self.group_number + ' has the following grades: '
        for x in self.grades:
            txt += str(x) + ' '
        return txt


def SortParam(st):
    return st.full_name


while True:
    try:
        number_of_students = int(input("How many students?\n"))
    except ValueError:
        print("It`s not number, please enter the NUMBER of students ")
    else:
        break

students = []
for i in range(number_of_students):
    pattern_full_name = "[a-zA-Z]"
    full_name = input("Write the fullname:\n")
    while True:
        if (re.search(pattern_full_name, full_name)):
            break
        else:
            full_name = input("Wrong name!!!Write the fullname again:\n")

    pattern_group_number = "[1-4]"
    group_number = input("write the number of group from 1 to 4:\n")
    while True:
        if (re.search(pattern_group_number, group_number)) and 1 <= int(group_number) <= 4:
            break
        else:
            group_number = input("Wrong group number!!!Write the group number again:\n")

    while True:
        try:
            n = int(input("Hom much grades?\n"))
        except ValueError:
            print("It`s not number, please enter how many grades ")
        else:
            break
    print("Write the student`s grades line by line:")
    grades = []
    for i in range(n):
        while True:
            try:
                score = int(input())
            except ValueError:
                print("It`s not number, please enter the number ")
            else:
                break

        grades.append(score)
    st = Student(full_name, group_number, grades)
    students.append(st)

print("Student list:")
for st in students:
    print(st)

students = sorted(students, key=SortParam)

print("sorted students:")
for st in students:
    print(st)

print("bad students:")
n = 0
for st in students:
    for val in st.grades:
        if val < 3:
            print(st)
            n += 1
            break
if n == 0:
    print("there are not students with bad grades")
