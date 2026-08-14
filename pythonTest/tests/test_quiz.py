import importlib.util
from pathlib import Path

# 动态从文件路径加载被测试模块，因为文件名包含特殊字符
module_path = Path(__file__).resolve().parents[1] / 'python基础2' / '流程控制-综合案例.py'
spec = importlib.util.spec_from_file_location("quiz_module", str(module_path))
quiz = importlib.util.module_from_spec(spec)
spec.loader.exec_module(quiz)
play_game = quiz.play_game


def make_input(seq):
    it = iter(seq)

    def _input(prompt=''):
        try:
            return next(it)
        except StopIteration:
            return ''

    return _input


def test_win_all():
    inputs = ['print', 'and', '解释型']
    out = []
    res = play_game(max_tries=3, input_func=make_input(inputs), print_func=out.append)
    assert res is True
    assert any('恭喜你通关了' in s for s in out)


def test_quit_mid():
    inputs = ['print', 'q']
    out = []
    res = play_game(max_tries=3, input_func=make_input(inputs), print_func=out.append)
    assert res is False
    assert any('您已经退出游戏' in s for s in out)


def test_fail_after_three():
    inputs = ['x', 'y', 'z']
    out = []
    res = play_game(max_tries=3, input_func=make_input(inputs), print_func=out.append)
    assert res is False
    assert any('挑战失败' in s for s in out)


def test_empty_input_not_counted():
    inputs = ['', 'print', 'and', '解释型']
    out = []
    res = play_game(max_tries=3, input_func=make_input(inputs), print_func=out.append)
    assert res is True
