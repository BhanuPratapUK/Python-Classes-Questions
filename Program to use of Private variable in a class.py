class Msg:
    def __init__(self,var1,var2):
        self.var1 = var1
        self.__var2= var2
    def display(self):
        print('The vlaue of the first number is -->',self.var1)
        print('The vlaue of the second number is -->',self.__var2)
x = Msg(10,20)
x.display()
print('The vlaue of the first number is -->',x.var1)
print('The vlaue of the private method outside of the class is -->',x.Msg__var2)