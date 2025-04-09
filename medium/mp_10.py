
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง
# โดยให้ผลลัพธ์ที่ได้คือ [(1, 10), (2, 20), (3, None), (4, None)]
# โดยไม่ต้องใช้ for loop
# โดยให้ผลลัพธ์ที่ได้คือ [(1, 10), (2, 20), (3, None), (4, None)]
# โดยไม่ต้องใช้ for loop
# โดยใช้ zip_longest จาก itertools
# โดยไม่ต้องใช้ zip

"""
    a = [1, 2, 3, 4]
    b = [10, 20]
    zipped = zip(a, b)
    print(list(zipped))  # ผลลัพธ์ไม่ครบทุกตัว จะแก้ไขยังไง?
"""

# คำตอบ:
from itertools import zip_longest

a = [1, 2, 3, 4]
b = [10, 20]
zipped = zip_longest(a, b, fillvalue=None)
print(list(zipped))