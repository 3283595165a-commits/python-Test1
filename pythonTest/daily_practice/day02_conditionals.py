"""Day 2 练习：条件分支与布尔判断

目标：
- 掌握 if/elif/else 的基本结构
- 理解条件表达式和布尔逻辑
- 学会根据输入做不同的程序分支
"""


def check_number(number):
    if number > 0:
        print(f"{number} 是正数")
    elif number < 0:
        print(f"{number} 是负数")
    else:
        print(f"{number} 是零")


def grade_score(score):
    if score < 0 or score > 100:
        print("成绩必须在 0～100 之间")
    elif score >= 90:
        print("成绩优秀")
    elif score >= 75:
        print("成绩良好")
    elif score >= 60:
        print("成绩及格")
    else:
        print("成绩不及格")


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} 是闰年")
    else:
        print(f"{year} 不是闰年")


def exercise_conditional():
    print("=== 检查数字 ===")
    check_number(10)
    check_number(-5)
    check_number(0)

    print("\n=== 成绩等级 ===")
    grade_score(95)
    grade_score(80)
    grade_score(65)
    grade_score(50)

    print("\n=== 闰年判断 ===")
    is_leap_year(2020)
    is_leap_year(1900)
    is_leap_year(2000)


def exercise_user_input():
    print("\n=== 用户输入练习 ===")

    try:
        number = int(input("请输入一个整数："))
        check_number(number)
    except ValueError:
        print("输入无效，请输入一个整数。")

    try:
        score = float(input("请输入成绩（0～100）："))
        grade_score(score)
    except ValueError:
        print("输入无效，请输入一个有效的成绩。")

    try:
        year = int(input("请输入年份："))
        is_leap_year(year)
    except ValueError:
        print("输入无效，请输入一个有效的年份。")


if __name__ == "__main__":
    exercise_conditional()
    exercise_user_input()