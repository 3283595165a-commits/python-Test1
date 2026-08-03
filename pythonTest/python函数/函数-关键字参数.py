#关键字参数：调用函数是，通过形参名=值的形式传递实参。位置参数跟关键字参数不能混用
#调用函数是，根据参数在函数定义中出现的顺序，把实参的值依次传递给对应的形参
def greet(name,gander,age,height):
    print(f'我叫{name},性别{gander},年龄{age},身高是{height}cm\n')
greet(age='50',height='580',name='米帅',gander='男')