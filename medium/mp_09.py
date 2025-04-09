
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง
# โดยให้ class B เรียก __init__ ของ class A ด้วย
# โดยที่ไม่ต้องแก้ไข class A

"""
    class A:
        def __init__(self, x):
            self.x = x

    class B(A):
        def __init__(self, y):
            self.y = y  # ไม่เรียก __init__ ของ A จะแก้ยังไง?
"""

# คำตอบ:
class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x, y):
        super().__init__(x)  # เรียก __init__ ของ A
        self.y = y

obj = B(10, 20)
print(obj.x)  # 10
print(obj.y)  # 20
