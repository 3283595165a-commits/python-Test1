"""答题闯关挑战赛（可单元测试的重构版）

规则：
- 一共三个关卡，每关一道题，答对进入下一关，三关都答对则挑战成功
- 每题最多有若干次尝试（默认 3 次），用户输入为空不消耗机会
- 输入 `q` 可随时退出

模块提供 `play_game` 函数，接受可替换的 `input_func` 与 `print_func` 以便测试。
"""

QUESTIONS = [
    ("python中用于输出的函数是？", "print"),
    ("python中用于表示逻辑“并且”的关键字是？", "and"),
    ("python属于是编译型还是解释型", "解释型"),
]


def play_game(max_tries=3, input_func=input, print_func=print):
    """运行答题闯关游戏。

    返回 True 表示通关成功，False 表示中途退出或挑战失败。
    """
    print_func('欢迎来到：答题闯关挑战赛（输入q可随时退出） \n')

    for level, (question, answer) in enumerate(QUESTIONS, start=1):
        print_func(f'*****第{level}关*****')
        tries = 1
        while tries <= max_tries:
            user_input = input_func(question)
            if user_input == answer:
                print_func('回答正确 \n')
                break
            if user_input == '':
                print_func('您的输入为空，请重新作答！\n')
                continue
            if user_input == 'q':
                print_func('您已经退出游戏！\n')
                return False
            # 错误答案
            leave = max_tries - tries
            if leave > 0:
                print_func(f'回答错误，您还剩{leave}次机会！\n')
                tries += 1
                continue
            else:
                print_func(f'挑战失败，本题的答案是：{answer},游戏结束！')
                return False

    print_func('恭喜你通关了')
    return True


if __name__ == '__main__':
    play_game()