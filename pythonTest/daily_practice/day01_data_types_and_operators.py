"""Day 1 练习：数据类型与运算符

目标：
- 熟悉整数、浮点数、字符串、布尔值
- 掌握基本算术运算、比较运算和逻辑运算
- 了解类型转换与字符串拼接

练习说明：
- 你可以直接运行这个脚本查看输出
- 也可以在每个函数中修改输入值，观察结果变化
"""


def exercise_arithmetic():
    a = 10
    b = 3
    print(f"整数运算：{a} + {b} = {a + b}")
    print(f"浮点数运算：{a} / {b} = {   a / b}")
    print(f"取余运算：{a} % {b} = {a % b}") 
    print('加法',a+b)
    print('减法',a-b)
    print('乘法',a*b)
    print('除法',a/b)
    print('整除',a//b)
    print('幂运算',a**b)
    print('取余',a%b)
def exercise_comparison():
    x = 5
    y = 10
    print(f"{x} > {y} : {x > y}")
    print(f"{x} < {y} : {x < y}")
    print(f"{x} == {y} : {x == y}")
    print(f"{x} != {y} : {x != y}")
    print(f"{x} >= {y} : {x >= y}")
    print(f"{x} <= {y} : {x <= y}")
def exercise_logic():
    p = True
    q = False
    print(f"{p} and {q} : {p and q}")
    print(f"{p} or {q} : {p or q}")
    print(f"not {p} : {not p}")
def exercise_string():
    name='python'
    version=3.9
    print('字符串拼接：' + name + ' ' + str(version))
    print('格式化输出：'f'欢迎学习{name} {version}')
    print('字符串长度：', len(name))
    print('首字母：', name[0])
    print('切片：', name[1:4])