class pappu:
    def __init__(self,s1,s2,s3):
        self.s1=s1
        self._s2=s2
        self.__s3=s3
    def fuck(self):
        print(self.__s3)

obj=pappu(1,2,3)
print(obj.s1)
print(obj._s2)
obj.fuck()
