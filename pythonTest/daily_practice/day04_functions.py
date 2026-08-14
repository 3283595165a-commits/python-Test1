"""Day 4 练习：函数与参数

目标：
- 理解函数定义与调用
- 掌握位置参数、关键字参数和默认参数
- 学习返回值和可变参数的使用
- 了解局部变量与全局变量的作用域
"""


def greet(name):
    """
    greet 函数：一个简单的问候函数。
    它接收一个姓名作为参数，并打印出个性化的问候语。
    这个函数展示了函数如何接收并使用参数。

    参数:
        name (str): 接收一个字符串，代表要问候的人的姓名。
    """
    print(f"你好，{name}！欢迎学习函数。")  # 打印带有传入姓名的问候语


def add(a, b):
    """
    add 函数：执行两个数字的加法运算。
    它接收两个数字作为参数，并返回它们的和。
    这个函数演示了函数如何接收多个参数并返回一个结果。

    参数:
        a (int/float): 第一个加数。
        b (int/float): 第二个加数。

    返回:
        int/float: 参数 a 和 b 的和。
    """
    return a + b  # 返回 a 和 b 的和


def format_score(name, score=0):
    """
    format_score 函数：格式化并打印学生的成绩。
    它接收学生的姓名和一个可选的成绩参数。如果未提供成绩，则默认为 0。
    这个函数展示了如何使用默认参数，使得函数调用更加灵活。

    参数:
        name (str): 学生的姓名。
        score (int/float, optional): 学生的成绩。默认为 0。
    """
    print(f"学生 {name} 的成绩是: {score} 分")  # 打印学生的姓名和成绩


def sum_all(*numbers):
    """
    sum_all 函数：计算任意数量数字的总和。
    它使用可变参数 *numbers，可以接收零个或多个位置参数。
    这个函数演示了如何处理不确定数量的输入参数。

    参数:
        *numbers (int/float): 任意数量的数字参数。

    返回:
        int/float: 所有传入数字的总和。
    """
    total = 0  # 初始化总和为 0
    for n in numbers:  # 遍历所有传入的数字
        total += n  # 将每个数字加到总和中
    return total  # 返回计算出的总和


def describe_person(name, age, **info):
    """
    describe_person 函数：描述一个人的详细信息。
    它接收姓名、年龄作为位置参数，并使用 **info 接收任意数量的关键字参数。
    这展示了如何使用关键字可变参数来处理灵活的额外信息。

    参数:
        name (str): 人的姓名。
        age (int): 人的年龄。
        **info (dict): 额外的关键字信息，例如 爱好='篮球', 学校='北京大学'。
    """
    print(f"姓名: {name}")  # 打印姓名
    print(f"年龄: {age}")  # 打印年龄
    for key, value in info.items():  # 遍历所有的额外信息
        print(f"{key}: {value}")  # 打印键值对


def exercise_functions():
    """
    exercise_functions 函数：整合并演示各种函数的使用。
    它调用 greet, add, format_score, sum_all, describe_person 函数,
    展示了函数定义、参数传递（位置参数、默认参数、可变参数、关键字参数）和返回值。
    """
    print("=== 函数定义与调用 ===")
    greet("小明")  # 调用 greet 函数进行问候
    result = add(7, 8)  # 调用 add 函数，将返回值存储在 result 变量中
    print(f"7 + 8 = {result}")  # 打印 add 函数的计算结果

    print("\n=== 默认参数 ===")
    format_score("小红")  # 调用 format_score，使用默认成绩 0
    format_score("小李", 95)  # 调用 format_score，传入指定成绩 95

    print("\n=== 可变参数 ===")
    print(f"数字之和: {sum_all(1, 2, 3, 4, 5)}")  # 调用 sum_all，传入多个数字

    print("\n=== 关键字参数 ===")
    # 调用 describe_person，传入位置参数和关键字参数
    describe_person("小张", 20, 爱好="篮球", 学校="北京大学")


def exercise_scope():
    """
    exercise_scope 函数：演示 Python 中的作用域规则。
    它定义了一个外部变量和一个内部函数,
    展示了局部变量和全局变量在不同作用域中的访问和生命周期。
    """
    print("\n=== 作用域示例 ===")
    count = 10  # 这是一个局部变量，对于 inner 函数来说是外层（封闭）作用域的变量

    def inner():
        """
        inner 函数：定义在 exercise_scope 内部的嵌套函数，用于演示作用域。
        它可以访问外层函数的变量 (count)，并有自己的局部变量 (local_count)。
        """
        local_count = 5  # 这是一个局部变量，只在 inner 函数内部有效
        print("内层函数 local_count =", local_count)  # 打印 inner 的局部变量
        print("内层函数 count =", count)  # 打印外层函数的变量

    inner()  # 调用内层函数
    print("外层函数 count =", count)  # 打印外层函数的变量


if __name__ == "__main__":
    # 当脚本直接运行时，执行以下函数调用
    exercise_functions()  # 运行函数与参数的练习
    exercise_scope()  # 运行作用域的练习
