
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง
# โดยให้ฟังก์ชัน countdown(n) ทำงานได้ตามที่ต้องการ

"""
    def countdown(n):
        print(n)
        countdown(n-1) 

    countdown(5)
"""

# คำตอบ:
def countdown(n):

    if n == 0:
        return

    print(n)
    countdown(n-1)

countdown(5)

