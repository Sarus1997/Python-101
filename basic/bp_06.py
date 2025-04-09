# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง 
# โดยให้แสดงผลลัพธ์เป็น "Gender not found"

"""
    person = {"name": "Alice", "age": 25}
    print(person["gender"])
"""

# คำตอบ: 
person = {"name": "Alice", "age": 25}
if "gender" in person:
    print(person["gender"])
else:
    print("Gender not found")

# หรือ เพื่มค่า "gender" ลงใน dictionary person
person = {"name": "Alice", "age": 25, "gender": "female"}
print(person["gender"])

print(person["name" + "age" + "gender"])