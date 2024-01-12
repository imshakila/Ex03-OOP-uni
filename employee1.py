class Employee :
    def __init__(self, fname, lname, age, employee_num, salary ):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.stu_num = employee_num
        self.salary = salary

    def all_info(self) :
        print(f"Fname : {self.fname}, Lname : {self.lname}, 
        Age : {self.age}, Salary : {self.salary}")
    
    def show_info(self) :
        print(f"{self.fname} + {self.lname} is an employee ")

