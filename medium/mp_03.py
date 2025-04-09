
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง
# โดยไม่ต้องใช้คำสั่ง close() ในการปิดไฟล์
# โดยให้ใช้คำสั่ง with แทน

"""
    file = open("data.txt", "w")
    file.write("Hello")
    # ไม่มี file.close() อาจเกิดปัญหา ควรใช้โค้ดแบบไหนดี?
"""

# คำตอบ:
with open("medium/data.txt", "w") as file:
    file.write("Hello")