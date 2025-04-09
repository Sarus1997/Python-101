
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง
# โดยไม่ต้องเปลี่ยนแปลงโค้ดที่อยู่ใน with statement

"""
    with open("file.txt", "r") as file:
        data = file.read()

    print(file.read())  # IOError: ควรแก้ไขยังไง?
"""

# คำตอบ:
with open("medium/file.txt", "r") as file:
    data = file.read()

print(data)
