# # 健身计划循环脚本for循环案例
# # 外层循环：遍历1-30天
# for day in range(1, 31):
#     # 打印当天标题
#     print(f'*****第{day}天*****')
#     # 内层循环：每天3组训练
#     for group in range(1, 4):
#         print(f'这是第{group}组仰卧起坐')
#     # 每天训练完成提示（关键：缩进和内层for同级）
#     print(f'第{day}天任务已完成')

# # 全部30天完成后的总提示
# print(f'为期30天健身计划已完成')
# while循环案例
day=1
while day <=30:
    print(f'*****第{day}天*****')
    group =1
    while group <=4:
        print(f'*****这是第{group}组仰卧起坐')
        group +=1
    print(f'第{day}天任务已完成')
    day +=1
print('为期30天健身计划已完成')