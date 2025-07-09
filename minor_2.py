# class class1:
#     def __init__(self,name,age,height):
#         self.name=name
#         self.age=age
#         self.height=height
# o=class1("Piyush",21,158)
# print(o.name)
# print(o.age)
# print(o.height)


# class person:
#     # defult constructor
#     def __init__(self):
#         self.m = "Hello this is my first code"
#     def print(self):
#         print(self.m)
# o = person()
# o.print()

# class person2():
#     # parameterized constructor
#     def __init__(self,name,age):  #constructor created
#         self.name=name
#         self.age=age
#     def func(per):
#         print("Tne name is : " +per.name)
#         print("The age is : " +per.age)


# o=person2("Piyush","21")
# o.func()

# o.name="Mayank"
# o.age="26"
# print()
# o.func()

# class Student:
#     def __init__(self,name,m1,m2,m3):
#         self.name=name
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def avg(self):
#         print("The avg of",self.m1,self.m2,self.m3,"is : "+str(self.ans))
#     def calculation(self):
#         self.ans=(self.m1+self.m2+self.m3)//3

# o=Student("Piyush",1,2,3)
# o.calculation()
# o.avg()

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @staticmethod
#     def hello():
#         print("Hello")

# o=Student("Piyush",21)
# o.hello()


# ---------------------------------------X---X----X-------------------------------------------------

#  The down 3 code is for inharitance


# class Parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print (self.name,self.age)

# class Child(Parent):
#     pass

# o=Child("Piyush",21)
# o.display()


# class Parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print (self.name,self.age)

# class Child(Parent):
#     def __init__(self,name,age):
#         super().__init__(name,age)

# o=Child("Piyush",21)
# o.display()



# class Parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print (self.name,self.age)

# class Child(Parent):
#     def __init__(self,name,age):
#         Parent.__init__(self,name,age)

# o=Child("Piyush",21)
# o.display()

class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print ("Dear ",self.name,"Your age is ",self.age,"the the year difference is ",self.diff)

class Child(Parent):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.joining_year=year
        self.current_year=2025
        self.diff=self.current_year-self.joining_year


o=Child("Piyush",21,2004)
o.display()