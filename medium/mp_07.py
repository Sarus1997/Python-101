
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง
# โดยไม่ต้องใช้ global หรือ nonlocal

"""
    x = 10
    def change():
        x += 5  # UnboundLocalError: จะแก้ไขยังไง?

    change()
    print(x)
"""

# คำตอบ:
x = 10
def change():
    global x
    x += 5 

change()
print(x)
