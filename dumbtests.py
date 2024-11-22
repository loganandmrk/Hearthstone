class Class1:
    def __init__(self, hello):
        self.hello = hello

class Class2:
    def __init__(self, hello):
        self.hello = hello

class Class3(Class1, Class2):
    def __init__(self, hello, goodbye):
        Class1.__init__(self, hello)
        Class2.__init__(self, hello)

class3 = Class3("goodbye", "hello")
print(class3.hello)