"""Day 5 练习：文件 I/O 与异常处理

目标：
- 掌握使用 with open() 安全地读取和写入文本文件
- 学习 try-except-else-finally 异常处理结构
- 理解常见的文件/输入输出异常（FileNotFoundError, IOError）
- 练习记录简单的日志信息并进行错误处理
"""

import os


def read_file_example(filepath):
    """
    读取文件内容并打印。
    展示如何使用 with 语句安全地打开文件以及如何捕获 FileNotFoundError 异常。

    参数:
        filepath (str): 要读取的文件路径。
    """
    print(f"\n--- 尝试读取文件: {filepath} ---")
    try:
        # 使用 with 语句确保文件在读取完毕后自动关闭
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            print("文件内容读取成功：")
            print(content)
    except FileNotFoundError:
        print(f"【错误】文件 {filepath} 不存在！请检查路径是否正确。")
    except Exception as e:
        print(f"【错误】读取文件时发生未知错误: {e}")


def write_file_example(filepath, content):
    """
    向文件写入内容（会覆盖原内容）。
    展示如何写入文本，并在捕获到异常时进行提示。

    参数:
        filepath (str): 写入的文件路径。
        content (str): 要写入的文本内容。
    """
    print(f"\n--- 尝试写入文件: {filepath} ---")
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"成功将内容写入到 {filepath}")
    except IOError as e:
        print(f"【错误】写入文件时发生 I/O 错误: {e}")
    except Exception as e:
        print(f"【错误】写入文件时发生未知错误: {e}")


def append_log_example(filepath, log_message):
    """
    以追加模式向文件写入日志信息，并演示完整的 try-except-else-finally 流程。

    参数:
        filepath (str): 日志文件路径。
        log_message (str): 日志消息内容。
    """
    print(f"\n--- 尝试追加日志到文件: {filepath} ---")
    f = None
    try:
        # 'a' 模式代表追加（Append）
        f = open(filepath, "a", encoding="utf-8")
        f.write(log_message + "\n")
    except IOError as e:
        print(f"【错误】追加写入日志失败: {e}")
    else:
        # 如果没有发生异常，则执行 else 块
        print("日志追加写入成功！")
    finally:
        # 无论是否发生异常，finally 块都会执行
        # 在这里进行手动的资源释放（虽然推荐 with，但此例为了演示 finally 的清理作用）
        if f is not None:
            f.close()
            print("文件资源已在 finally 块中安全关闭。")


def exercise_file_io_and_exceptions():
    """
    执行文件 I/O 与异常处理的综合练习。
    """
    test_dir = "temp_practice"
    # 创建一个临时练习目录（如果不存在）
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    target_file = os.path.join(test_dir, "practice.txt")
    log_file = os.path.join(test_dir, "app.log")

    # 1. 尝试读取一个不存在的文件，触发异常处理
    read_file_example(os.path.join(test_dir, "non_existent.txt"))

    # 2. 写入一些初始化内容
    initial_content = "Hello Python!\n这是第五天的文件 I/O 练习。\n我们正在学习如何读写文件和处理异常。"
    write_file_example(target_file, initial_content)

    # 3. 再次读取刚才写入的文件，验证内容
    read_file_example(target_file)

    # 4. 追加多条日志，演示追加模式和 finally 结构
    append_log_example(log_file, "[INFO] 2026-08-14 10:30:00 - 用户登录成功")
    append_log_example(log_file, "[WARNING] 2026-08-14 10:31:15 - 磁盘空间不足")
    append_log_example(log_file, "[ERROR] 2026-08-14 10:32:50 - 数据库连接超时")

    # 5. 读取日志文件并显示
    read_file_example(log_file)

    # 清理临时创建的练习文件（保留目录结构，只清理内容，或保持原样供学习者查看）
    print("\n--- 练习结束，临时文件已保留在 'temp_practice' 目录下，供您查看和复习。 ---")


if __name__ == "__main__":
    exercise_file_io_and_exceptions()
