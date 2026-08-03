#调用函数是，根据参数在函数定义中出现的顺序，把实参的值依次传递给对应的形参
def greet(name,gander,age,height):
    print(f'我叫{name},性别{gander},年龄{age},身高是{height}cm')
greet('米帅','男','50','580')