class ABC:
    val = 0
    def __init__(self,var):
        self.var = var
        ABC.val+=1
        print('The value of the variable is --->',var)
obj = ABC(10)
obj = ABC(20)
obj = ABC(30)
obj = ABC(40)
print('The Total variable values are aded is --->',ABC.val)