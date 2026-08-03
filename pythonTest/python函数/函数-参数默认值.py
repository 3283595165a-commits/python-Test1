#参数默认值：定义函数是，通过形参名=值的形式，为参数指定一个默认值
#注意：默认参数必须要放在必选参数的后面，或者说：某个形参，一旦设置了默认值，那它后面的所有形参也必须要写默认值！
def greet(name,gander,age,height,msg='你好'):
    print(f'我叫{name},性别{gander},年龄{age},身高是{height}cm')
    print(f'我想说：{msg}')
# greet('米帅','男',15,172)
greet('米帅','男',15,172,'hello')