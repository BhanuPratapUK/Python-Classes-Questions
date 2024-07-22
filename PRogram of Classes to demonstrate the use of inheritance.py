class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print('Name is -->',self.name)
        print('Age is -->',self.age)

class Teacher(Person):
    def __init__(self,name,age,department,qualifications):
        Person.__init__(self,name,age)
        self.department = department
        self.qualifications= qualifications
    def displayT(self):
        Person.display(self)
        print('The depatment in which I am working -->',self.department)
        print('The Qualifications I have --->',self.qualifications)

class Student(Person):
    def __init__(self,name,age,subject,roll_no):
        Person.__init__(self,name,age)
        self.subject = subject
        self.roll_no = roll_no
    def displayS(self):
        Person.display(self)
        print('The Subject iahv chossen-->',self.subject)
        print('The roll no i got in the class-->',self.roll_no)
A = Person('Bhanu Pratap',27)
A.display()
B= Teacher('Akash',30,'Management','B.Tech',)
B.displayT()
C= Student('Bhanu Pratap Sharan',28,'PCM',244,)
C.displayS()
print(Student.__base__)


