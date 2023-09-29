# 自訂 module, 一個 module 就是 .py 檔
# 建立 student.py
import student

stud1 = student.Student('賴麒祐', 50, 60 , 70)
print(stud1.chinese, stud1.english, stud1.math)
print(stud1.total(), stud1.average)
print(stud1)

stud2 = student.get_student('賴麒祐')
print(stud2.chinese, stud2.english, stud2.math)
print(stud2.total(), stud2.average)
print(stud2)