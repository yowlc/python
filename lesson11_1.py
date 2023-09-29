import random

# 取得 一個學生 的 成績 list
# numscore -> 一個學生要有幾個成績
def get_scores(numscore : int) -> list:
    scores = []
    for i in range(numscore):
        scores.append(random.randint(50, 100))
    return scores

def get_names(numstud : int) -> list:
    # 取得 姓名
    # 使用 with as, 會自動 close() 關檔
    with open('names.txt', encoding="utf-8", newline='') as file1:
        name_str = file1.read()

    # 字串 轉 list
    name_list = name_str.split(sep='\n')
    # 隨機取出 特定數量 的內容
    return random.choices(name_list, k=numstud)

numstud = int(input('請輸入學生數:'))
new_name_list = get_names(numstud)

all_student = []
for x in range(numstud):
    # 一個學生有 5 個 成績
    tmp_score = get_scores(5)
    # 使用 [str] 轉換成 list, ['aaa'] -> list
    all_student.append([new_name_list[x]] + tmp_score)

print(all_student)
