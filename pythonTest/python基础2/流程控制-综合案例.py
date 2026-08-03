#一共三个关卡（每个关卡只有一道题），答对进入下一关，3关都答对则挑战成功！
#1.答错可从事，每道题都有三次回答机会，若三次均打错，则挑战失败，游戏自动结束
#2.如果用户输入为空，则提示重新作答，且不浪费机会
#3.如果用户输入字母Q，则直接退出游戏
print('欢迎来到：答题闯关挑战赛（输入q可随时退出） \n')
#题目与答案
ques1 = 'python中用于输出的函数是？'
ans1 = 'print'
ques2= 'python中用于表示逻辑“并且”的关键字是？'
ans2= 'and'
ques3= 'python属于是编译型还是解释型'
ans3= '解释型'
#最多可尝试次数
max_tries =3
#总关卡书
total_levels =3
#是否处于可游戏状态
is_playing =True
#根据题目数量开始循环

for level in range(1, total_levels +1):
    #打印当前是第几关
    print(f'*****第{level}关*****')
    #取出当前关卡所对应的题目和答案
    if level ==1:
        question, answer = ques1, ans1
    elif level==2:
        question, answer = ques2, ans2
    else :
        question, answer = ques3, ans3
        #记录当前关卡尝试次数
    tries=1
    #若已经尝试的次数，小于等于最大尝试次数，则进入循环
    while  tries<=max_tries:
#向用户提问
        user_input = input(''+question)
        #根据用户的输入，来决定做什么
        if user_input == answer:
            print('回答正确 \n')
            break
        elif user_input =='':
            print('您的输入为空，请重新作答！\n')
            continue
        elif user_input =='q':
            print('您已经退出游戏！\n')
            is_playing =False
            break
        else:
            #计算剩余次数
            leave = max_tries - tries
            #判断是否还有剩余次数
            if leave >0 :
                print(f'回答错误，您还剩{leave}次机会！\n')
                tries+=1
                continue
            else:
                print(f'挑战失败，本题的答案是：{answer},游戏结束！')
                is_playing==False
    if is_playing == False:
        break
if is_playing == True:
    print('恭喜你通关了')