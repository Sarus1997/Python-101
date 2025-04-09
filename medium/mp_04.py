
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง
# โดยไม่ต้องเปลี่ยนแปลงโค้ดที่อยู่ในบรรทัดที่ 2

"""
    func = lambda x: if x > 0: "Positive" else: "Negative"
    # SyntaxError: จะต้องแก้ยังไง?
    print(func(5))
"""

# คำตอบ:
func = lambda x: "Positive" if x > 0 else "Negative"
print(func(5))

