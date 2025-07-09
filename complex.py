# class Comple:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def display(self):
#         print(self.real ,"+" ,self.img,"i")
#     def __add__(self,other):
#         real=other.real+self.real
#         img=self.img+other.img
#         return Comple(real,img)
# o=Comple(10,15)
# o.display()
# o1=Comple(20,5)
# o1.display()
# ans=o + o1
# ans.display()

class Item:
    def __init__(self,price):
        self.price=price
    def __gt__(self,other):
        if isinstance(other,Item):
            return self.price>other.price
        return NotImplemented

class Table(Item):
    pass
class Chair(Item):
    pass

t=Table(2500)
c=Chair(1500)
if(t>c):
    print("Table is more expensive then chair")
else:
    print("Chair is more expensive then table")