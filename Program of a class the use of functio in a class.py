def scale(x):
    return x*10
class ABC:
    def __init__(self,var):
        self.var = var
    def display(self):
        print('The value is-->',self.var)
    def modify(self):
        self.var = scale(self.var)
x = ABC(3)
x.display()
x.modify()
x.display()