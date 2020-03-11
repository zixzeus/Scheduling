import pandas as pd
import numpy as np
class Department():
    def __init__(self,dept_name,dept_id):
        self.dept_name = dept_name
        self.dept_id = dept_id

    def __str__(self):
        return self.dept_name


class Group():
    def __init__(self,group_name,group_id,dept=None):
        self.group_name = group_name
        self.group_id = group_id
        self.dept = dept

    def __str__(self):
        return str(self.dept)+","+str(self.group_id)


class Employee():
    def __init__(self,emp_name,emp_id,group=None,qualification=None):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.group = group
        self.qualification = []

    def __str__(self):
        return str(self.emp_id)+" "+str(self.emp_name)

    def get_dept_id(self):
        if self.group!=None:
            return self.group.dept.dept_id
        else:
            print("dept id error")

    def get_dept_name(self):
        if self.group!=None:
            return self.group.dept.dept_name
        else:
            print("dept name error")

    def set_group(self,new_group):
        self.group = new_group

    def get_group_id(self):
        if self.group != None:
            return self.group.group_id
        else:
            print("please set group")

    def get_qualification(self):
        return self.qualification

    def add_qualification(self,new_qualification):
        self.qualification.append(new_qualification)


class WorkerDepartment():
    def __init__(self,dept):
        self.groups_set = set()
        self.dept = dept

    def get_name(self):
        return self.dept.dept_name

    def add_dept_members(self,new_group):
        new_group.set_dept(self.dept)
        self.groups_set.add(new_group)

    def show_group_members(self):
        for _ in self.groups_set:
            print(_)


class WorkerGroup():
    def __init__(self,group,dept=None):
        self.members_set = set()
        self.group = group
        self.dept = dept

    def __str__(self):
        return str(self.group.group_name)

    def add_group_members(self,new_worker):
        new_worker.set_group(self.group)
        self.members_set.add(new_worker)

    def search_group_members(self,search_id):
        for worker in self.members_set:
            if worker.emp_id == search_id:
                return True

        else:
            return False

    def del_group_members(self,worker):
        if self.search_group_members(worker.emp_id):
            self.members_set.remove(worker)

    def set_dept(self,new_dept):
        self.dept = new_dept

    def show_members(self):
        for _ in self.members_set:
            print(_)


class EmployeeTable():
    def __init__(self,EmployeeInfo):
        self.EmployeeTable = EmployeeInfo

    def dept_select(self,dept):
        em_table = pd.read_excel(self.EmployeeTable, sheet_name=dept)
        return em_table


class EmployeeDynamic():
    def __init__(self):
        pass



# int1 = Department("international",1)
# ck = Department("check",2)
#
# gp1 = Group("happy",101)
# gp2 = Group("sad",102)
# gp3 = Group("sad",2)
#
# em1= Employee("lisi",1011)
# em2= Employee("wanger",1012)
#
# em3= Employee("fuck",1013)
# em4= Employee("love",1014)
# print(gp1)
# print(em1)
# print(em1.get_dept_id())
# print(em1.get_group_id())
# print(em1.get_qualification())
# em1.add_qualification("check in")
# print(em1.get_qualification())
# print(em1.get_dept_name())
# print("\n")
# w1 = WorkerGroup(gp1)
# w1.add_group_members(em1)
# w1.add_group_members(em2)
# w1.show_members()
# w2 = WorkerGroup(gp2)
# w2.add_group_members(em3)
# w2.add_group_members(em4)
# print("\n")
# print(em1.get_dept_name())
# print(em2.get_dept_name())
# print(em1.get_qualification())
# print(em2.get_qualification())
# print(w1.search_group_members(1011))
# print(w1.search_group_members(1200))
# print("\n")
# w1.del_group_members(em1)
# w1.show_members()
# print("\n")
# print(em1)
# dept1=WorkerDepartment(int1)
# dept1.add_dept_members(w1)
# dept1.add_dept_members(w2)
# dept1.show_group_members()
# print(dept1.get_name())