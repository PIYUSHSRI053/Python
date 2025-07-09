class Parson:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Parson):
    def __init__(self,employee_id,name,age):
        self.employee_id=employee_id
        Parson.__init__(self,name,age)
    def display(self):
        print("The name is", self.name)
        print("The age is", self.age)
        print("The empolyee Id is", self.employee_id)

obj=Employee(1001,"Piyush",21)
obj.display()