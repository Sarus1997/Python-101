
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง
# โดยให้ฟังก์ชัน multiply() สามารถรับอาร์กิวเมนต์ได้หลายตัว
# และคูณค่าทั้งหมดเข้าด้วยกัน
# โดยไม่ต้องระบุจำนวนอาร์กิวเมนต์ที่แน่นอน

"""
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    print(multiply())
"""

# คำตอบ:
def multiply(*args):
    if not args:
        return "No numbers provided"
    result = 1
    for num in args:
        result *= num
    return result

print(multiply())  # จะคืนค่า "No numbers provided"
print(multiply(2, 3))  # จะคืนค่า 6