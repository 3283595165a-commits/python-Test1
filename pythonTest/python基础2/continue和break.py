# continue:跳过本次循环剩余语句，随后进入下一次循环
# break：立即终止循环，不再执行后续循环
for day in range(1,5):
    print(f'*****第{day}天*****')
    print('吃饭')
    for item in range(1,3):
        print(f'面包{item}')
        if day ==4 and item ==2:
            continue
        print(f'牛奶{item}')
    print('睡觉')