#可变位置参数：
# 定义函数时，在形参名前加*，可以接受任意数量的位置参数，并打包成一个元组
#可变关键字参数：
#定义函数时，在形参名前加**，可以接收任意数量的关键字参数，并打包成一个字典
#注意！！！！！
#可变位置参数，可变关键字参数，可以同时使用，但必须先写可变位置参数
#定义函数（使用*args去接收：可变位置参数）
def test1(*aegs):
#此处args的值。是一种新的数据类型为元组"
    print(aegs)
#调用函数
test1('米帅','男',18,199)
#定义函数（使用**kwaegs去接收：可变关键字参数）
def test2(**kwargs):
    #此处kwargs的值，是一种新的数据类型，叫字典
    print(kwargs)
    #调用函数
test2(name='米帅', gander='男', age=48, hegiht=88)
#定义函数（同时使用：可变位置参数，可变关键字参数）
def test3(a,b,*args,c='米帅',**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
test3('张三','男','抽烟','喝酒',age=18,height=189)