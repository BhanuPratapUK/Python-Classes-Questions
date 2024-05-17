class employee():
    emplcount= 0
    def __init__(self,name,desig,salary):
        self.name = name
        self.desig= desig
        self.salary = salary
        employee.emplcount+=1
    def counting(self):
        print('There is %d employees in this organisation'% (employee.emplcount))
    def print(self):
        print('My self {} , my position is {} and my salary is {}'.format(self.name,self.desig,self.salary))
A= employee('Bhanu','team lead','2,50,000')
B= employee('Shivam','leader','2,25,000')
C= employee('Anu','teams','2,00,000')
D= employee('Anuj','manager','1,75,000')
E= employee('Akash','G.m','1,50,000')
A.print()
B.print()
C.print()
D.print()
E.print()
A.counting()