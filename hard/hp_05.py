
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง

"""
    class Meta(type):
        def __new__(cls, name, bases, dct):
            dct["greet"] = lambda self: "Hello"
            return super().__new__(cls, name, bases, dct)

    class MyClass(metaclass=Meta):
        pass

    obj = MyClass()
    print(obj.greet())  # ทำไมอาจเกิดปัญหา?

"""

# คำตอบ:
