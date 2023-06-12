# class MyClass:
#     x=5
# obj1=MyClass()
# print(obj1.x)

# class MyClass3:
#     b=13
#     c=44
#     def __init__(self,a):
#         self.a=a
#         print(self.a)
# object1=MyClass3
# object1.self.a


class Person:
    def __init__(self, name,age):
        self.name=name
        self.age=age

p1=Person("ramesh", 27)
print(p1)