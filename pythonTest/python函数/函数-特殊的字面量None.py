#1.None 是一个特殊的字面量，他表示：空值/无意义
msg=None
#2.None的类型是NoneType.
print(type(msg))
#3.None转为布尔值是False
print(bool(msg))
#4.None不能参与数学运算，也不能与字符串凭借。
if not msg:
    print('w')
#5.不给函数设置返回值，函数会默认返回None
