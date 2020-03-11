from SchedulingAlgorithm import PreScheduler,OnlineScheduler

import Plan


class MainScheduler():

    EmployeeInfo = []
    FlightInfo = []
    PreScheduler()
    while not SCHEOVER:
        OnlineScheduler()

    def scheover(self):
        global SCHEOVER
        SCHEOVER = True

class Student():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __str__(self):
        return str(self.id)+" "+str(self.name)


class ClassRoom():
    def __init__(self):
        self.members = set()

    def add_student(self,Student):
        self.members.add(Student)

    def show_members(self):
        for _ in self.members:
            print(_)


st1 = Student(1,"hello")
st2 = Student(2,"funny")
st3 = Student(3,"fuck")

mathclass = ClassRoom()
mathclass.add_student(st1)
mathclass.show_members()
print("\n")
mathclass.add_student(st2)
mathclass.add_student(st3)
mathclass.show_members()


