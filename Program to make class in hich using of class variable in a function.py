class adding:
    def __init__(self,var):
        self.var = var
    def display(self):
        print('Here is the value is after adding --->',self.var)
    def add(self):
        self.var+=2
        self.display()
x = adding(13)
x.add()