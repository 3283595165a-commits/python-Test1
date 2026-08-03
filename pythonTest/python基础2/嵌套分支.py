# 获取用户输入并转换类型
age = int(input('请输入你的年龄：'))
has_report = input('是否提交体检报告？（是/否）')
level = int(input('请输入你的会员等级[1/2/3]：'))

# 第一层判断：年龄是否符合参赛要求
if 18 <= age <= 45:
    print('你的年龄符合参赛要求')
    # 第二层判断：是否提交体检报告
    if has_report == '是':
        print('你的体检报告已提交')
        # 第三层判断：会员等级对应的奖励
        if level == 1:
            print('你获得纪念T恤')
        elif level == 2:
            print('你获得跑鞋一双')
        elif level == 3:
            print('你获得运动耳机一副')
        else:
            print('无效的会员等级')  # 补充异常等级提示
    elif has_report == '否':
        print('你还没有提交体检报告')
    else:
        print('请输入“是”或“否”回答体检报告问题')  # 补充输入格式提示
else:
    print('你的参赛年龄不符合参赛要求')