import importlib.util
import traceback
from pathlib import Path

# 加载测试文件
module_path = Path(__file__).resolve().parent / 'test_quiz.py'
spec = importlib.util.spec_from_file_location('test_quiz', str(module_path))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

# 收集并运行以 test_ 开头的函数
failures = []
for name in dir(mod):
    if name.startswith('test_'):
        func = getattr(mod, name)
        if callable(func):
            try:
                func()
                print(f'{name}: OK')
            except AssertionError as e:
                print(f'{name}: FAIL')
                traceback.print_exc()
                failures.append(name)
            except Exception:
                print(f'{name}: ERROR')
                traceback.print_exc()
                failures.append(name)

if failures:
    print(f"\n{len(failures)} tests failed: {failures}")
    raise SystemExit(1)
else:
    print('\nAll tests passed')
