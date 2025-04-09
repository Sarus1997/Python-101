
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง

"""
    import pickle

    class Data:
        def __init__(self, value):
            self.value = value

    obj = Data(100)
    data = pickle.dumps(obj)

    class Data:  # เปลี่ยนโครงสร้างคลาสใหม่
        def __init__(self, value, extra):
            self.value = value
            self.extra = extra

    print(pickle.loads(data))  # อะไรอาจผิดพลาด?
"""

# คำตอบ:
