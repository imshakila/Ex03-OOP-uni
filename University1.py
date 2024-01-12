from stu1 import *
from employee1 import *
class University :
    def __init__(self, name) :
        self.name = name
        self.students = []
        self.employees = []

    def add_stu(self, stu) :
        self.student.append(stu)
        print("added !")
        
    def remove_stu(self, stu_num) :
        for i in self.students :
            if i.stu_num == stu_num :
                self.students.remove(i)
                break

    def edit_stu(self, stu_num = None) :
        self.stu_num = stu_num or self.stu_num
        print("edited !")

    def search_stu(self, stu_num) :
        for i in  self.student :
            if i.stu_num == stu_num:
                return i
        return None



