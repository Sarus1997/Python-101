
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง

"""
    import weakref

    class Example:
        pass

    obj = Example()
    ref = weakref.ref(obj)

    del obj
    print(ref())  # ค่าควรเป็นอะไร? และทำไม?

"""

# คำตอบ:
