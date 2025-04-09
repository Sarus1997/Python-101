
# โจทย์: แก้ไขโค้ดต่อไปนี้ให้ถูกต้อง
# โดยให้โค้ดทำงานได้ทั้งใน Windows และ Linux
# และให้ทำงานได้ทั้งในรูปแบบของ Thread และ Process
# โดยไม่ให้เกิดข้อผิดพลาดใดๆ

"""
    import multiprocessing
    import threading

    def worker():
        print("Working")

    if __name__ == "__main__":
        for _ in range(5):
            t = threading.Thread(target=worker)
            p = multiprocessing.Process(target=worker)
            
            t.start()
            p.start()
            
            t.join()
            p.join()

"""

# คำตอบ:
import multiprocessing
import threading

def worker():
    print("Working")

if __name__ == "__main__":
    for _ in range(5):
        t = threading.Thread(target=worker)
        p = multiprocessing.Process(target=worker)
        
        t.start()
        p.start()
        
        t.join()
        p.join()

