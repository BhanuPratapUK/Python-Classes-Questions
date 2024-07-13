class ABC:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def __repr__(self):
        return repr(self.name)
    def __len__(self):
        return len(self.name)
text = ABC('Bhanu Pratap',30)
print('The string representation of the age is -->',repr(text))
print('The length name is-->',len(text))