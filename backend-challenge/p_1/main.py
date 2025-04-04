## จงหาเส้นทางที่มีค่ามากที่สุด

#  - ซึ่งจะอยู่ใน Array ดังต่อไปนี้ [[59], [73, 41], [52, 40, 53], [26, 53, 6, 34]]
#  - โดยเส้นทางที่มีค่ามากที่สุดจะเป็นตามจุดสีแดง
#  - แต่ละ node ห้ามย้อนกลับ (ต้องขึ้นลงเป็นทางเดียว) และเชื่อมกัน
#  - คำตอบให้อยู่ในรูปของ จำนวนรวมของเส้นทางที่ผ่าน ซึ่งจากตัวอย่างคือ 237
#  - ให้เขียนโปรแกรมภาษา Python โดยใช้ input จากไฟล์ data/hard.json

## Test case
#  - input = [[59], [73, 41], [52, 40, 53], [26, 53, 6, 34]] output = 237
#  - input = data/hard.json output = 7273

import json

def find_max_path_sum(triangle):
    dp = [row[:] for row in triangle]
    for row in range(len(dp) - 2, -1, -1):
        for col in range(len(dp[row])):
            dp[row][col] += max(dp[row + 1][col], dp[row + 1][col + 1])
    return dp[0][0]

with open("data/hard.json", "r") as f:
    data = json.load(f)

print("Max path sum:", find_max_path_sum(data))
