class parent:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber


    def display(self):
        print("name of person is",self.name,"and idnumber is",self.idnumber)


#child class
class employee(parent):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        super().__init__(name,idnumber)

emp1=employee("Ali",1234,20000,"intern")
emp1.display()
print("salary of Ali is",emp1.salary)


