class Student :
    def __init__(self, fname, lname, age, stu_num, scores) :
        self.fname = fname
        self.lname = lname
        self.age = age
        self.stu_num = stu_num
        self.scores = scores

    def all_info(self) :
        print(f"Fname : {self.fname}, Lname : {self.lname}, 
        Age : {self.age}, Scores : {self.scorse}")
    
    def show_info(self) :
        print(f"{self.fname} + {self.lname} is a student " )

