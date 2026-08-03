# a=100
# b=200

# def test():
#     c="尚硅谷"
#     d="你好啊"
#     global a#全局变量声明
#     a=300
#     print('函数中的打印（a）',a)
#     print('函数中的打印（b）',b)
#     print('函数中的打印（c）',c)
#     print('函数中的打印（d）',d)
# # test()
# # print('******************************')
# # print('全局的打印(a)',a)
# # print('全局的打印（b）',b)
# # #局部作用域和局部变量，会在函数调用时创建，在函数执行结束后自动销毁
# def test2():
#     m=300
#     m+=1
#     print(f'我是test2函数中打印的m：{m}')
# test2()
# test2()
# #全局作用域和全局变量，会在程序开始时创建，在程序结束后销毁
n=100
def test3():
    global n
    n+=1
    print(f'我是test函数中打印的n：{n}')
test3()
test3()
test3()
print(n)