"""Day 3 练习：循环结构

目标：
- 掌握 while 循环和 for 循环的区别与应用场景
- 理解循环控制语句 break 和 continue 的作用
- 练习使用嵌套循环实现经典算法（如九九乘法表）
"""


def exercise_while():
    """while 循环通常用于未知循环次数，满足特定条件时运行。"""
    print("=== while 循环练习 从1+到100===")
    total = 0
    i=1
    while i <=100:
        total += i
        i+=1
    print(f"1 加到 100 的结果是: {total}")

def exercise_for():
    """for 循环通常用于已知循环次数，遍历序列或范围。"""
    print("=== for 循环练习 从1+到100===")
    total = 0
    for i in range(1, 101):
        total += i
    print(f"1 加到 100 的结果是: {total}")

    print("\n---for 循环：遍历 range(5)---")
    for i in range(5):
        print(f"当前数字: {i}")
    print("\n---for 循环：遍历列表---")
    fruits = ['苹果', '香蕉', '橘子']
    for idx,fruit in enumerate(fruits):
        print(f"第 {idx+1} 个水果是: {fruit}")

def exercise_break_continue():
    """break 用于提前退出循环，continue 用于跳过当前迭代。"""
    print("=== break 与 continue 练习 ===")
    print("\n---使用 break 退出循环---")
    numbers=[12,13,14,15,16]
    for num in numbers:
        if num ==15:
            print("遇到 15，退出循环")
            break
    print("\n---使用 continue 跳过当前迭代---")
    for i in range(1, 6):
        if i == 3:
            print("遇到 3，跳过当前迭代")
            continue
        print(f"当前数字: {i}")

def exercise_multiplication_table():
    """嵌套循环实现九九乘法表。"""
    print("=== 九九九乘法表 ===")
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j} x {i} = {i * j}", end="\t")
        print()  # 换行


def exercise_user_input_loop():
    """while 循环的一个经典用法：持续接收用户输入，直到输入 q 退出"""
    print("\n=== 用户输入循环练习 ===")
    total = 0
    while True:
        user_input = input("请输入一个整数（输入 'q' 退出）：")
        if user_input.lower() == 'q':
            print("退出循环")
            break
        try:
            number = int(user_input)
            total += number
            print(f"你输入的整数是: {number}")
        except ValueError:
            print("请输入有效的整数或 'q' 退出。")
    print(f"所有输入的整数之和是: {total}")


if __name__ == "__main__":
    exercise_while()
    exercise_for()
    exercise_break_continue()
    exercise_multiplication_table()
    exercise_user_input_loop()