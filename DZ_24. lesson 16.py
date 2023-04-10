class MyClass:
    class_attribute_1 = "I am class attribute No1"
    class_attribute_2 = "I am class attribute No2"

    def __init__(self, x=0):
        self.x = x

    @staticmethod
    def method_static_1():
        print("I am staticmethod No 1 and I don't contact with object")

    @staticmethod
    def method_static_2():
        print("I am staticmethod No 2 and I don't contact with object too")


a = MyClass()
b = MyClass(9)
MyClass.method_static_1()
a.method_static_2()
print(MyClass.class_attribute_1)
print(MyClass.class_attribute_2)
print('*'*50)
print(a.class_attribute_1)
a.class_attribute_1 = "I am class attribute No1 changed by 'a'"
print(a.class_attribute_1)
print(b.class_attribute_1)
print('*'*50)
print("MyClass attribute:", MyClass.class_attribute_2)
print("MyClass attribute from a:", a.class_attribute_2)
print("MyClass attribute from b:", b.class_attribute_2)
