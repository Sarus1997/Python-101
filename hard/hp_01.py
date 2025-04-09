
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง
# โดยให้ `a.value` ยังคงเป็น 10 หลังจากที่ `b.value` ถูกเปลี่ยนเป็น 20
# โดยใช้ `copy.deepcopy` เพื่อทำการคัดลอกอ็อบเจ็กต์
# โดยไม่ให้มีการแชร์ข้อมูลระหว่าง `a` และ `b`

"""
    import copy

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    a = Node(10)
    b = copy.deepcopy(a)
    b.value = 20

    print(a.value)  # ค่าของ `a.value` ควรเป็นอะไร? ทำไมถึงเป็นเช่นนั้น?

"""

# คำตอบ:
import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(10)
b = copy.deepcopy(a)
b.value = 20

print(a.value)

