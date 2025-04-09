
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง

"""
    class Resource:
        def __del__(self):
            print("Resource cleaned up!")

    def create():
        obj = Resource()

    create()
    import gc; gc.collect()  # `__del__` จะถูกเรียกหรือไม่?
"""

# คำตอบ:
