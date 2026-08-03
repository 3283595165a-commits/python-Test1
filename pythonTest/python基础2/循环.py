#while循环 
print('你需要回答问题，答题成功才能走出去')
answer='中国人'
riddle = '你是什么人'
guess = ''
while guess!=answer:
    print(f'问题：{riddle}')
    guess=input('请输入答案：')
    if guess==answer:
        print('回答正确')
    else:
        print('回答错误')