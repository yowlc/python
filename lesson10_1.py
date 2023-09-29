import random

def allNames() -> list:
    with open('names.txt', encoding="utf-8") as file1:
        name_list = []
        for x in file1:
            name_list.append(x.replace('\n', ''))
            # name_list.append(x[:3])
    
    return name_list

# print(name_list[152])

print('===== 命名系統 =====\n\n')
while True :
    name_list = allNames()

    # 隨機 串列 抓 幾筆
    first_name = input('請輸入 姓:')
    counts = int(input('請輸入筆數:'))
    list1 = random.choices(name_list, k=counts)
    for x in list1:
        print(first_name + x[-2:])

    isagain = input('是否繼續嗎?(y/n)')
    if isagain.lower() == 'n':
        break

print('結束')