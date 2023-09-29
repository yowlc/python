import random
while True:
    min = 1
    max = 100
    target = random.randint(min, max)
    print(target)
    count = 0
    print('------猜數字------\n')

    while True:
        keyin = int(input(f'猜數字的範圍{min}~{max}:'))
        count += 1
        if (keyin < min) or (keyin > max):
            print('輸入超出範圍')
        else:
            if (keyin == target):
                print(f'猜對了, 數字是:{target}, 總共猜了{count}次')
                break
            else:
                print(f'輸入的數是{keyin}, 猜錯了, 已經猜了{count}次, ', end='')
                if keyin > target:
                    max = keyin - 1
                    print('再小一點')
                else:
                    min = keyin + 1
                    print('再大一點')

    play_again = input('要繼續嗎?(y or n)')
    if play_again == 'n':
        break
    else:
        continue

print('遊戲結束..')