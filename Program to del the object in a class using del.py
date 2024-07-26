class ABC:
    def __init__(self,val):
        self.val= val
    def display(self):
        print('The value is --<>',self.val)
x= ABC(1000)
x.display()
x.new1= 10
print(x.new1)
x.new2= 20
print(x.new2)
del x.new1
print(x.new2)
print(x.new1)