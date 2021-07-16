class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


class C(A, B):
    def __init__(self):
        super().__init__()
    
    def showprop(self):
        print(self.foo)
        print(self.bar)
        print(self.name)

'''
Python uses method resolution order to look it up in the class. The lookup starts in the current class but doesn't define the name attribute. 
Python will look at the order in which it is defined. Since A is listed first we see Class A instead of Class B.
'''

c = C()
c.showprop()
print(C.__mro__) #This will show the method resolution order. 