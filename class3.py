class MyClass1:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    # def __str__(self):
    #     return f"{self.name}({self.age})"
    def __str__(self):
        print("printing")
        return "test"

p1=MyClass1("Ramesh",22)
print(p1)