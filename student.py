# 建立 實體
# 提供 變數, module
# 提供 function

class Student:
    # 實體的 attribute 屬性
    def __init__(self, name="無名氏", chinese=99, english=99, math=99):
        self.name    = name
        self.chinese = chinese
        self.english = english
        self.math    = math

    # 實體的 method 方法
    def total(self) -> int:
        return self.chinese + self.english + self.math
    
    # 建立 property 屬性, 類似 method, 沒有參數, 一定要傳出一個值
    @property
    def average(self) -> float:
        return round(self.total() / 3.0, 2)
    
    def __repr__(self):
        return f'我是student實體, 我叫{self.name}'

import random
# 隨機 建立 學生的 3個成績    
def get_student(n:str) -> Student:
    ch = random.randint(50, 100)
    en = random.randint(50, 100)
    ma = random.randint(50, 100)
    return Student(name=n, chinese=ch, english=en, math=ma)
