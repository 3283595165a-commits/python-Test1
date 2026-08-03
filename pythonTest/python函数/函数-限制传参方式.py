#具体规则：/前边只能用位置参数，*后面只能用关键字参数
#/和*同时出现时，/必须在*前面
def greet(name,/,gander,*,age,height):
    print(f'我叫{name},性别{gander},年龄{age},身高是{height}cm\n')
greet('米帅','男',age='50',height='580')